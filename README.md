# ST101 Programming for Data Science

## Final Project (Mark received: 86/100)

### 2022/23 Michaelmas Term

---

## Tasks

1. Cipher using the functional programming approach
   * In [crypto.py](crypto.py), write the function definition for the function encode() and decode()
   * In [report.ipynb](report.ipynb), demonstrate the use of the two functions
2. Investigate if the "Success paradox" is observed using a movie dataset.
   * From https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata, two csv files which contain information about 4803 movies were downloaded, merged and simplified.
   * Investigate whether some "generalised friendship paradox" discussed in the paper "Generalized friendship paradox in complex networks: The case of scientific collaboration" is observed in the data, namely whether in general for actors, their co-actors are more "successful" than them in terms of the number of appearances in movies and also the average revenue.
3. Create players with different strategies to play the number guessing game we have seen in Workshop 2
  * Consider 3 simple strategies: select at random, select the smallest and select the mid. 
  * Consider a strategy inspired by reinforcement learning.


A report in a Jupyter Notebook in [`report.ipynb`](report.ipynb) is attached to demonstrate my programs and summarise my result.

---
## Concepts/tools must_ use

Must_ use _all_ of the following in the project _appropriately_:

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
