#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Please read instructions below!!

from sympy import FiniteSet
from rich.console import Console
import typer

TODO = None
# Group member Names
# 1. Add Your Name Here
# 2. Add Your Name Here
# 3. Add Your Name Here
# 4. Add Your Name Here

# Note: Each person must turn in own activity using the code from group work.

# Create a Typer object to support the command-line interface
cli = typer.Typer()

@cli.command()
def main()->None:
    """ driver function """

    console = Console()

    # Add your group's lists below
    list1 = TODO
    list2 = TODO
    list3 = TODO
    list4 = TODO

    # Print up all lists
    print(f"lists:\n 1 -> {list1}\n 2 -> {list2}\n 3 -> {list3}\n 4 -> {list4}\n")

    # Create sets from lists
    set1 = TODO
    set2 = TODO
    set3 = TODO
    set4 = TODO

    # Find the Union of all sets from the group
    union_set = TODO
    console.print("Union:", union_set)

    # Intersection of all sets from the group
    intersection_set = TODO
    print("Intersection:", intersection_set)

    # Difference between first set and second sets from the group (you can determine which sets these are actually!)
    differences = TODO
    console.print("Difference (Set1 - (Set2)):", differences)

    # Similarities between same chosen sets from above
    simTwoSets = TODO
    console.print("Similarities between Set?? and Set?? : {simTwoSets}")

    # Difference between all sets and one chosen set (Hint: code is of form: s1.difference(set2, ..., set4)
    difference_allToOneset = TODO
    console.print("Difference (Set1 - (Set2 ∪ Set3 ∪ Set4)):", difference_allToOneset)

    # Difference between all sets and different chosen set 
    difference_set2 = TODO
    console.print("Difference (Set2 - (Set1 ∪ Set3 ∪ Set4)):", difference_set2)

    # Difference between all sets and different chosen set 
    difference_set3 = TODO
    console.print("Difference (Set3 - (Set1 ∪ Set2 ∪ Set4)):", difference_set3)

    # Difference between all sets and different chosen set 
    difference_set4 = TODO
    console.print("Difference (Set4 - (Set1 ∪ Set2 ∪ Set3)):", difference_set4)

# end of main()