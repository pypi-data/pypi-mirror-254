import string
import time
from typing import List

import requests
from ase.build import bulk
from ase import Atoms
import numpy as np
from matplotlib import pyplot as plt

from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    TimeElapsedColumn
)

from rich.live import Live
from rich.console import RenderableType, Group
from rich.tree import Tree

HOST = "relax.rothchild.me"
PORT = "60123"

def serialize_atoms(atoms):
    atoms_dict = atoms.todict()
    for key in atoms_dict:
        if isinstance(atoms_dict[key], np.ndarray):
            atoms_dict[key] = atoms_dict[key].tolist()
    return atoms_dict

def job_status(job_id):
    url = f"http://{HOST}:{PORT}/job_status"
    response = requests.get(url, json={"job_id": job_id}).json()
    return response

class ExtensibleGroup(Group):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.is_stale : bool = True

    def add_elem(self, new_renderable: RenderableType) -> None:
        self._renderables = self._renderables + (new_renderable,)
        self.is_stale = True

    @property
    def renderables(self) -> List["RenderableType"]:
        if self._render is None or self.is_stale:
            self._render = list(self._renderables)
            self.is_stale = False
        return self._render

class PartialFormatter(string.Formatter):
    def __init__(self, missing='~'):
        self.missing = missing

    def format_field(self, value, spec):
        if value is None:
            return self.missing
        else:
            return super(PartialFormatter, self).format_field(value, spec)

class NoneFormatter:
    def __init__(self, format_string):
        self.fmt = PartialFormatter()
        self.format_string = format_string

    def format(self, *args, **kwargs):
        return self.fmt.format(self.format_string, *args, **kwargs)

def stream_job(job_id):
    status = job_status(job_id)
    tree = Tree(status["progress"]["title"])
    with Live(tree, refresh_per_second=2) as live:
        branches = {}
        progress_groups = {}
        progress_bars = {}
        while True:
            status = job_status(job_id)
            progress = status["progress"]

            def update_tree(tree, path, progress):
                for child in progress["children"]:
                    branch_path = path + (child["id"],)
                    if branch_path in branches:
                        branch = branches[branch_path]
                    else:
                        branch = tree.add(child["title"])
                        branches[branch_path] = branch

                        # make sure progress_group is the last branch on the tree
                        if len(tree.children) > 1:
                            tree.children.append(tree.children.pop(-2))

                    update_tree(branch, branch_path, child)

                if path in progress_groups:
                    progress_group = progress_groups[path]
                else:
                    progress_group = ExtensibleGroup()
                    tree.add(progress_group)
                    progress_groups[path] = progress_group

                def transformed_val(tracked_val):
                    # transform from raw values to 0-1 progress range
                    v = tracked_val["value"]
                    start_v = tracked_val["initial_value"]
                    end_v = tracked_val["target_value"]

                    if v is None or start_v is None or end_v is None:
                        return 0

                    # whether we want to increase or decrease v
                    sign = (end_v - start_v) / abs(end_v - start_v)

                    if sign * v <= sign * start_v:
                        return 0
                    if sign * v >= sign * end_v:
                        return 1

                    if tracked_val["scale"] == "log":
                        v = np.log(v)
                        start_v = np.log(start_v)
                        end_v = np.log(end_v)

                    progress = (v - start_v) / (end_v - start_v)
                    return progress

                for tracked_val in progress["tracked_values"]:
                    pbar_path = path + (tracked_val["title"],)

                    if pbar_path in progress_bars:
                        progress_bar = progress_bars[pbar_path]
                    else:
                        if tracked_val["target_value"] is None:
                            raw_value_fmt = NoneFormatter(
                                "{task.fields[raw_value]:.7g} " +
                                "{task.fields[units]}"
                            )
                            progress_bar = Progress(
                                SpinnerColumn(),
                                TextColumn("{task.description}"),
                                TextColumn(raw_value_fmt),
                                TimeElapsedColumn()
                            )
                        else:
                            progress_fmt = NoneFormatter(
                                "{task.fields[raw_value]:.4g} " +
                                "{task.fields[units]}"
                                " / " +
                                "{task.fields[target_value]} " +
                                "{task.fields[units]}"
                            )

                            progress_bar = Progress(
                                TextColumn("{task.description}"),
                                BarColumn(),
                                TaskProgressColumn(),
                                TextColumn(progress_fmt),
                                TimeElapsedColumn()
                            )
                        progress_group.add_elem(progress_bar)
                        progress_bar.add_task(
                            tracked_val["title"],
                            total=1,
                            units=tracked_val["units"],
                            raw_value=None,
                            target_value=tracked_val["target_value"]
                        )
                        progress_bars[pbar_path] = progress_bar

                    progress_bar.update(
                        0,
                        completed=transformed_val(tracked_val),
                        raw_value=tracked_val["value"]
                    )

            update_tree(tree, (), progress)

            if status["is_complete"]:
                break
            time.sleep(1)

def get_job_result(job_id):
    url = f"http://{HOST}:{PORT}/job_result"
    response = requests.get(url, json={"job_id": job_id}).json()
    if response["job_type"] == "energy_job":
        return EnergyResult(response["result"])
    elif response["job_type"] == "relax_job":
        return RelaxResult(response["result"])
    elif response["job_type"] == "bands_job":
        return BandStructureResult(response["result"])
    else:
        raise ValueError("Unknown job type")

class EnergyResult:
    def __init__(self, result):
        self.energy = result["total_energy"]
        self.fermi_energy = result["fermi_energy"]
        self.energy_units = result["energy_units"]
        self.kpoints = result["kpoints"]

    def __repr__(self):
        return f"EnergyResult(energy={self.energy:.4f} {self.energy_units})"

class RelaxResult:
    def __init__(self, result):
        self.energy = result["energy"]
        self.energy_units = result["energy_units"]
        self.relaxed_atoms = Atoms.fromdict(result["relaxed_atoms"])

    def __repr__(self):
        return (f"RelaxResult(energy={self.energy:.4f} {self.energy_units}, "
                f"atoms=...)")

def energy(atoms):
    atoms_dict = serialize_atoms(atoms)
    args = {"atoms": atoms_dict,
            "kpoints_conv_ev": 0.01}
    response = requests.post(f"http://{HOST}:{PORT}/energy", json=args).json()
    print(response)
    job_id = response["job_id"]
    stream_job(job_id)
    return get_job_result(job_id)

class ForcesResult:
    def __init__(self, forces):
        self.forces = forces

def forces(atoms):
    return ForcesResult(np.zeros_like(atoms.get_positions()))

def relax_structure(atoms, kpoints=None):
    if kpoints is None:
        kpoints = [4, 4, 4]
    args = {"atoms": serialize_atoms(atoms),
            "kpoints": kpoints}
    response = requests.post(f"http://{HOST}:{PORT}/relax", json=args).json()

    job_id = response["job_id"]
    stream_job(job_id)
    return get_job_result(job_id)

class BandStructureResult:
    def __init__(self, result):
        self.energy_results = EnergyResult(result["energy_results"])
        self.relax_results = RelaxResult(result["relax_results"])
        self.k_xvals = np.array(result["k_xvals"])
        self.energies = np.array(result["energies"])
        self.energy_units = result["energy_units"]
        self.highsym_xvals = np.array(result["highsym_xvals"])
        self.highsym_labels = result["highsym_labels"]

    def __repr__(self):
        labels = "".join(self.highsym_labels)
        return f"BandStructureResult({labels})"

    def plot(self):
        plt.plot(self.k_xvals, self.energies.T, color="k")
        for x in self.highsym_xvals:
            plt.axvline(x)
        plt.xticks(ticks=self.highsym_xvals, labels=self.highsym_labels)

        plt.axhline(self.fermi_energy, linestyle="--", label="Fermi Energy")
        plt.legend()

        plt.ylabel("Energy (eV)")
        plt.xlabel("k-point")
        plt.show()

    @property
    def fermi_energy(self):
        return self.energy_results.fermi_energy

def band_structure(atoms, bz_path=None):
    args = {"atoms": serialize_atoms(atoms),
            "relax_first": True,
            "bz_path": bz_path}
    response = requests.post(f"http://{HOST}:{PORT}/bands", json=args).json()
    job_id = response["job_id"]
    stream_job(job_id)
    return get_job_result(job_id)
