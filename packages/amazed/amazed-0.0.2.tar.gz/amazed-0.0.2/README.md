# amazed

Maze generation & solver in one. Simply put, just _a maze(d)_.
**Still in active development!**

Capable of both generating mazes of any rectangular size and solving them using various algorithms.

## Generation
There are multiple ways of creating a maze:
* Depth First Search using recursion
* Hunt and Kill
* Binary Tree
* Random Kruskal
* Aldous Broder
* Random Carving
* Boulder (also named Cinnamon Bun)
## Solvers
- Depth First Search 
- Depth First Search Randomized
- Depth First Search Heuristic
- Lee
- A*
## Visualization
Each generated maze can be exported either as a simple image (all possible formats from `pillow`) or as a GIF (_will be available `v0.0.3`_), where the carving process can be observed. For solvers, each one can be exported either as an image or as a GIF, with a red line (the color is configurable) displaying the chosen path.