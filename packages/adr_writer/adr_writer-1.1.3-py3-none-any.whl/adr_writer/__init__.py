#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""Write ADRs from technical solutioning discussions."""
import sys
import re
from datetime import datetime, timezone
from typing import Union


__version__ = "1.1.3"


def questions() -> dict:
    """Define questions."""
    return {
        "problem_exists": "Is there really a problem (y/N)?: ",
        "problem_statement": "Problem statement: ",
        "solution": "- Option: ",
        "tool": "\t- Platform: ",
        "tool_available": "\t- Is platform available (y/N)?: ",
        "solution_pro": "\t\t- Pro: ",
        "solution_con": "\t\t- Con: ",
        "proposal" : "- Proposed option: ",
        "justification": "\t- Justification: ",
        "consequence": "\t- Consequence: ",
        "info": "- More information: ",
        "other_consideration": "- Other consideration: "
    }


def solutions() -> dict:
    " Get problem details from questions."
    question_dict = questions()
    solution = input(question_dict["solution"]).strip()
    tool = input(question_dict["tool"]).strip()
    tool_available = input(question_dict["tool_available"]).strip()
    pro = input(question_dict["solution_pro"]).strip()
    con = input(question_dict["solution_con"]).strip()

    return {
        "solution": solution,
        "tool": tool,
        "tool_available": tool_available,
        "pro": pro,
        "con": con
    }


def project() -> dict:
    """Define project."""
    name = input("Name: ").strip()
    id = input("ID: ").strip()
    description = input("Description: ").strip()
    owner = input("Decider: ").strip()
    architect = input("Author: ").strip()
    deadline = input("Deadline: ").strip()
    budget = input("Budget: ").strip()
    
    return {
        "name": name,
        "id": id,
        "description": description,
        "owner": owner,
        "architect": architect,
        "deadline": deadline,
        "budget": budget
    }


def parse_bool(
    answer: str
) -> bool:
    """Parse boolean answer."""
    return (
        True
        if re.match(
            r"^y$",
            answer,
            re.IGNORECASE
        )
        else False
    )


def write_report(
    result_dict: dict,
    project_dict: dict
) -> None:
    """Write report to file."""
    with open(
        f"{project_dict['id']}-{project_dict['name'].lower().replace(' ', '-')}.md",
        "w",
        encoding="latin-1"
    ) as file:

        # Write project overview.
        file.write("----\n")
        file.write("- Status: \n")
        file.write(f"- Date: {datetime.now(timezone.utc).strftime('%B %d, %Y %H:%M:%S')} (UTC)\n")
        file.write(f"- Decider: {project_dict['owner']}\n")
        file.write(f"- Author: {project_dict['architect']}\n")
        file.write(f"- Deadline: {project_dict['deadline']}\n")
        file.write(f"- Budget: {project_dict['budget']}\n")
        file.write("----\n")
        file.write("\n")

        # Write problem description.
        file.write(f"# {project_dict['name']}\n\n")

        file.write("## Description\n\n")
        file.write(f"{project_dict['description']}\n\n")

        file.write("## Problem Statement\n\n")
        file.write(f"{result_dict['problem_statement']}\n\n")

        # Write solutions.
        file.write("## Considered Options\n\n")
        for solution in result_dict["solutions"]:
            file.write(f"- {solution['solution']}\n")
        file.write("\n")

        # Write proposal.
        file.write("## Decision Outcome\n\n")
        file.write(f"{result_dict['proposal']}\n")
        for justification in result_dict["justifications"]:
            file.write(f"- {justification}\n")
        file.write("\n")

        # Write consequences.
        file.write("### Consequences\n\n")
        for consequence in result_dict["consequences"]:
            file.write(f"- {consequence}\n")
        file.write("\n")

        # Write pros and cons.
        file.write("## Pros and Cons of the Options\n\n")
        for solution in result_dict["solutions"]:
            file.write(f"### {solution['solution']}\n\n")
            file.write(f"- Platform: {solution['tool']}\n")
            file.write(f"- Platform available: {solution['tool_available']}\n")

            # Write pros.
            file.write("- Pros\n")
            for pro in solution["pro"]:
                file.write(f"\t- {pro}\n")

            # Write cons.
            file.write("- Cons\n")
            for con in solution["con"]:
                file.write(f"\t- {con}\n")
            
            file.write("\n")

        file.write("\n")

        # Write more information.
        file.write("## More Information\n\n")
        for info in result_dict["more_information"]:
            file.write(f"- {info}\n")
        file.write("\n")

        # Write other considerations.
        file.write("## Alternative Considerations\n\n")
        for other in result_dict["other_considerations"]:
            file.write(f"- {other}\n")
        file.write("\n")


def main():
    print(f"\nADR Writer {__version__}")
    print("- All fields are required.")
    print("- Hit Enter to escape looping questions.\n")

    # Define project and get the questions to ask.
    project_dict = project()
    question_dict = questions()

    print(" ")
    # Get problem statement.
    problem_statement = input(question_dict["problem_statement"]).strip()
    print(" ")
    # Do we really have a problem?
    if parse_bool(input(question_dict["problem_exists"]).strip()):

        # Get solutions and stop if there is no more.
        solution_list = []

        print(" ")
        solution = input(question_dict["solution"]).strip()

        while solution != "":
            solution_dict = {"solution": solution}
            solution_dict["tool"] = input(question_dict["tool"]).strip()
            solution_dict["tool_available"] = parse_bool(
                input(question_dict["tool_available"]).strip()
            )

            # Get solution pros and stop if there is no more.
            pro_list = []

            print(" ")
            pro = input(question_dict['solution_pro']).strip()

            while pro != "":
                pro_list.append(pro)
                pro = input(question_dict['solution_pro']).strip()

            solution_dict["pro"] = pro_list

            # Get solution cons and stop if there is no more.
            con_list = []

            print(" ")
            con = input(question_dict['solution_con']).strip()

            while con != "":
                con_list.append(con)
                con = input(question_dict['solution_con']).strip()

            solution_dict["con"] = con_list

            solution_list.append(solution_dict)

            print(" ")
            solution = input(question_dict["solution"]).strip()

        # Make a decision.
        print(" ")
        proposal = input(question_dict["proposal"]).strip()

        # Get justifications and stop if there is no more.
        justification_list = []

        print(" ")
        justification = input(question_dict["justification"]).strip()

        while justification != "":
            justification_list.append(justification)
            justification = input(question_dict["justification"]).strip()
        
        # Get consequences and stop if there is no more.
        consequence_list = []

        print(" ")
        consequence = input(question_dict["consequence"]).strip()

        while consequence != "":
            consequence_list.append(consequence)
            consequence = input(question_dict["consequence"]).strip()

        # Get more information and stop if there is no more.
        info_list = []

        print(" ")
        info = input(question_dict["info"]).strip()

        while info != "":
            info_list.append(info)
            info = input(question_dict["info"]).strip()
        
        # Get pther considerations and stop if there is no more.
        other_list = []

        print(" ")
        other_consideration = input(question_dict["other_consideration"]).strip()

        while other_consideration != "":
            other_list.append(other_consideration)
            other_consideration = input(question_dict["other_consideration"]).strip()

        result_dict = {
            "problem_statement": problem_statement,
            "solutions": solution_list,
            "proposal": proposal,
            "justifications": justification_list,
            "consequences": consequence_list,
            "more_information": info_list,
            "other_considerations": other_list
        }

        # Write report to file.
        write_report(
            result_dict,
            project_dict
        )

    else:
        print("No problem to solve.")

    print(" ")
