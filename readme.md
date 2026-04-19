## **Advanced Graphing Calculator & Equation Solver**

## **Overview**

This **Advanced Graphing Calculator** is a comprehensive Python application developed over a **9-day intensive sprint in March 2026**. It represents a significant step forward in combining mathematical computation with data visualization and persistent storage.

The project bridges the gap between raw calculation and visual representation, allowing users to solve complex algebraic expressions while simultaneously generating high-quality coordinate graphs.

---

## **Core Features**

* **Symbolic Arithmetic**: Handles standard math operations, roots, and powers using the `SymPy` library for exact precision.  
* **Algebraic Expression Solver**: Automatically parses and solves for variables (e.g., `3x = 12`) using implicit multiplication logic (typing `3x` instead of `3*x`).  
* **Dynamic Graphing Engine**: Generates 2D function plots with a locked \-20 to 20 grid, featuring axis lines and dashed-style plotting for better visibility.  
* **Persistent History**: Implements **JSON-based File Handling** to save every calculation, ensuring your work is never lost between sessions.  
* **Automated Cleanup**: Includes built-in file management to delete temporary graph images and refresh the workspace.

---

## **Running on PythonAnywhere**

This calculator is specially configured for headless environments like **PythonAnywhere** using the `Agg` backend for Matplotlib.

1. **Upload files**: Upload the script and ensure you have a `calculator_history.json` file in the same directory (the script will create one if it’s missing).  
2. **Bash Console**: Open a new Bash console and run:

python3 main\_calculator.py

3.   
4. **Viewing Graphs**:  
   * After choosing option **"c"** and entering a function, the script saves a file named `temporary_graph.png`.  
   * To see your graph, go to the **Files** tab in PythonAnywhere and click on `temporary_graph.png` to view the image in your browser.

---

## **How to Use**

* **Option A (Arithmetic)**: Enter standard problems like `(5*5)/2`.  
* **Option B (Expressions)**: Enter algebraic equations like `4x - 10 = 0`.  
* **Option C (Graphing)**: Enter functions like `x**2 + 3`. Check your file folder for the resulting `.png` file.  
* **Option D/E (History)**: Access the JSON database to view your last result or your entire calculation history.  
* **Option F (Maintenance)**: Use this to wipe the current `temporary_graph.png` before creating a new visualization.

---

## **Technical Note**

This project was the culmination of a month-long deep dive into **Matplotlib** and **File Handling**.

* **Matplotlib Integration**: Learned how to utilize `lambdify` to convert symbolic expressions into NumPy-ready functions for rapid plotting.  
* **Data Persistence**: Focused on the `json` module to bridge the gap between Python dictionaries and permanent local storage.  
* **Implicit Parsing**: Implemented `standard_transformations` to make the user interface feel more natural for mathematical input.

---

