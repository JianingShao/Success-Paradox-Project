# ST101 Programming for Data Science

## Final Project

### 2022/23 Michaelmas Term

---

## Objectives

The project serves as the most important coursework for us to assess your progress in the course in terms of:
* Understanding of the course materials
* Ability to apply the course materials on real life problems using programming
* Other skills like problem solving and self learning skills

To allow us to be able to assess the qualities above, you are asked to complete 3 programming tasks (with 2 parts in Q3) and write a report to demonstrate your programs and summarise your results (See the section `Tasks` for more details). You are also required to use the programming concepts/tools listed under the section `Concepts/tools you must use` to show that you are capable of applying _all_ (or most) of the programming concepts/tools we have learned in this course.

---

## Tasks

1. Cipher using the functional programming approach. See [crypto.md](crypto.md) for further instructions
2. Investigate if the "Success paradox" is observed using a movie dataset. See [success_paradox.md](success_paradox.md) for further instructions
3. Create players with different strategies to play the number guessing game we have seen in Workshop 2
  * Consider 3 simple strategies: select at random, select the smallest and select the mid. See [number_guessing_game.md](number_guessing_game.md) for further instructions
  * Consider a strategy inspired by reinforcement learning. See [number_guessing_game_reinforcement.md](number_guessing_game_reinforcement.md) for further instructions


**All the code must be submitted.**

You are also required to write a report in a Jupyter Notebook in [`src/report.ipynb`](src/report.ipynb) to demonstrate your programs and summarise your result.

For each task, you must state clearly in the report where the corresponding code is (if it is not in the report and the location is not specified by the corresponding question). For other things you need to include in the report for task 1-3, please refer to the corresponding instructions.

---
## Concepts/tools you _must_ use

You _must_ use _all_ of the following in your project _appropriately_:

* Basics: control flow and appropriate use of containers
* Functions: abstraction and decomposition
  * Your submission must include at least one function
* Modules: modularisation
  * Your submission must have at least one .py file serves as a module and import at least one module / library
* At least one library not demonstrated (but it can be _mentioned_) in the course is used
  * E.g. `matplotlib`
* Good practice: testing, assertion, use of comments, etc
  * Your submission must include testing on at least one function
* OOP: encapsulation, abstraction, composition, inheritance (when appropriate)
* Functional programming: recursion, pure functions, use of higher order functions, immutable data (objects and variables not changed)
* Important data science tools including `Numpy` and/or `Pandas` with vectorised operations and Jupyter Notebook
  * Note using `NumPy` _or_ `Pandas` is enough, although you can use both if you want to

See the marking criteria below for more details.

If you think that some concepts/tools above are not appropriate for what you want to do, please contact the lecturer and we will see if such omission can be accepted, or alternative arrangement can be made.

---
## Knowledge that you _may_ consider to demonstrate

* Debugging
* Error raising and handling

---

## List of modules / libraries / data structures that you can use

You can use the tools below without getting permission from the lecturer:

* `random` and any of the functionality provided by it
* `functools.reduce()` (for Q1 only)
* `json.load()` (for Q2 only)
* `set` and any of the functionality provided by it
* `Pandas` and `Numpy`, but you can only use them for the tasks that specified that you can use them
* `matplotlib` library

For any "optional" or "additional" functionality / analysis that you want to add, there is no restriction on what you can use.

For any other modules / libraries / data structure / unseen built-in methods that you want to use, please get the permission from the lecturer. Moodle may also keep a list of approved modules / libraries / data structure / unseen built-in methods so please have a look as well. You will be penalised if you are using unauthorised modules / libraries / data structure / unseen built-in functions, etc. in your project.
