# Recursive Floyd Warshall Algorithm

This project presents a Python implementation of the Floyd-Warshall algorithm using recursion. The algorithm computes the shortest paths in a directed graph, handling both positive and negative edge weights effectively, as long as there are no negative cycles.

## Installation

1. Clone this repository
2. Change to root directory

```bash
cd floyd-warshall
```

3. Install necessary dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run unit tests:

```bash
  python -m _tests_.unit
```

Run performance tests:

```bash
  python -m _tests_.performance
```

Running recursive function

To run the recursive function module, use the following command:

```bash
  python -m functions.recursive
```

(Note: Running this command will not produce any output as the function does not inherently print anything, you need to modify the script as necessary.)

## Contributing

Pull requests are welcome. Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
