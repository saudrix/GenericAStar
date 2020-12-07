# Generic AStar :stars:

![Supported Python Versions](https://img.shields.io/badge/Python-3.9.0-blue.svg?logo=python&logoColor=white)  ![Made withJupyter](https://img.shields.io/badge/Jupyter-6.1.5-orange.svg?logo=jupyter&logoColor=white)  ![GitHub license](https://img.shields.io/badge/License-DTFW-green.svg?logo=GitHub%20Sponsors&logoColor=white)

------

The Generic A* Repository is made to release the search algorithm project of my final year in engineering school.  As you might have guessed, this repository contains an A* implementation. The goal of the project was to enhance the algorithm in any way we wanted. I choose to try and make the more generic implementation possible allowing the user to define his own problems and node structure according to a given template. And then compute the A* algorithm on the project of his choosing.

## How to use GA*​

### Global architecture 

~~~bash
```
Project
│   demo.py
│   Interacive.ipynb
|
├───core
│   │   AStar.py
│   │   GenericNode.py
│   │   Metrics.py
│
├───customMetrics
│   │   depth.py
│   │   time.py
│   │   wide.py
│   
├───customNodes
│   │   CityNode.py
│   │   TaquinNode.py
```
~~~

- The **demo** and **interactive** files are the main file to use if you want to understand and play with GA*.

- In the *core* folder, you can investigate the base class for **Nodes** and **Metrics** class and of course the main A* loop.

- In the *customNode* folder, you'll find two node example one for the **Taquin** and the other for a **TSP** graph solving problem. You can take inspiration from these to start implementing your own nodes.
- Finally the *customMetrics* folder contains basic A* **metrics** you can build upon to define you own.

### Getting started

Two ways you can start playing with GA*:

- Clone the repository and execute the demo folder
- Clone the repository and launch the interactive **Jupyter **:telescope: file.

The first technique is better if you have good knowledge of the A* algorithm and **Python** :snake: classes especially inheritance mechanism. You can use the next part of this file to gain a better understanding of my node and metric structure.

The interactive file is a jupyter notebook design to display the mechanisms of the GA* repository and facilitate the creation of a new problem step by step. It's designed to be really starter worthy mixing code parts and description of the deferent mechanisms involve.

## Generic Nodes and how to implement your own

The Generic Node class is a light blueprint describing the Node structure supported by GA*. To create your own *customNode*  create a class inheriting from Generic Node.

Some methods will need to be implement in order for your node to work. In case of an oversight on your behalf the base class should raise a specific error allowing you to easily correct your custom node.

### __repr\_\_

A **representation**, even a minimalistic one, is needed in order for you node to be displayed and for the GA* to show you the reconstructed resolution path.

### GetNeighbors 

The **GetNeighbors** method should describe how you travel in your graph from a node to the next. For example: imagine a labyrinth made of squared spot. Your neighbors can be the 4 or 8 spots next to you that aren't walls.

### SetHCost

The **SetHCost** method is used to compute the heuristic needed by the classic A* algorithm. If you don't want to compute an heuristic you can always set you H cost to be zero. The GA* would then computes as a Dijkstra implementation. In order to compute your heuristic, the method is given a **target** :red_circle: which is the end node given to the computeAstar function. Your method must compute an undermining estimate of the remaining distance to be traveled in your graph.

:warning: **Warning**: This setHCost method isn't designed to return the h value. you must assigned the *self.h* attribute of your node while in the scope of this function. Otherwise the GA* will behave as a Dijkstra pathfinder and might be much slower.

There is no limitation in the number of heuristic you can implement, you just need to ensure that only one is used as the *SetHCost* method of your node.

### Dist

The **Dist** method is passed another node as parameter. It must return the distance between the two nodes considered. 

For example: In a grid like problem where you move one spot at a time the *Dist* method might always return one, but in a more complex problem let's say a road networks, the *Dist* method is expected to compute the time represented to travel this road. It can be the distance between the two points joined by the road but it might also consider the speed limit or even traffic on this segment .

:warning: Remember, the algorithm might prefer the fastest way, the more accurate your distance between two nodes, the better the algorithm will be at giving you the real best solution in your graph.

## Generic Metrics and how to implement your own

### Implementation

To implement a metric for the GA* algorithm, you need to create a child of the **Metric** class. In this *customMetric* object you can add any parameters you like, the only two things you need are:

- A given parameter name to be passed to the super() constructor.
- A compute method that return a tuple of the form (self.name, your metric value for this iteration)

The name must be receive upon instantiation and given to the mother class. The compute method can access all Metric parameters including:



- **status** (bool) : is the A* computation over or not
- **iteration** (int): what iteration of the algorithm is currently going on
- **opened** ([Node]): a copy of the A* openSet for the given iteration
- **closed** ([Node]): a copy of the A* closedSet for the given iteration

The compute method can use all of these data and also custom attributes given to the specific metric child class. The only obligation is to return a tuple containing first the class name and second a value of the metric computation. 

### Usage

Once you've made your custom metric nothing else is required. In order to use it, you only need to instantiate it and give it the computeAStar method as a new metric. The search loop will update the contained data and call the compute method at every iteration and automatically store the results.

## Launching the A* computation

After creating a custom node and may be custom metrics, you can now use the GA* algorithm for your problem. To do it instantiate all the nodes your problem requires select a **start node** and an **objective** (end node). Then you can call the *ComputeAStar* method as follows:

```python
from core.AStar import ComputeAStar
ComputeAStar(startNode, endNode, verbose = False, *Metrics)
```

#### Inputs

The method require:

- **startNode** (GenericNode): the start location in your problem graph
- **endNode** (GenericNode): The targeted place in your graph
- **verbose** (boolean): enables metrics display for each iteration
- ***Metrics** (*args* Metric): A given set of custom metrics

#### Outpus

When the GA* end its computation, it should output two things:

- A table containing all the relevant metrics step (i.e. the existing value metrics excluding *None* values).
- A series of nodes showing the shortest path in you graph leading from the desired output to the start location.



<p align="center">
    <img src='https://ensc.bordeaux-inp.fr/sites/default/files/upload/page-edito/inp/img/logos/logo.ensc-bxinp.jpg' width=200px height=150px />
</p>
