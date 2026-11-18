# Documentation

| File / folder | Content |
| ------------- | ------- |
| [concept.md](concept.md) | Goal, components and data flow of the project |
| [decisions/](decisions/) | Short notes on important decisions ("why X instead of Y") |
| [diagrams/](diagrams/) | draw.io diagrams (`*.drawio.svg`) |

## Diagrams

**draw.io**: for free-form drawings (architecture, concepts).

- Install the VS Code extension *Draw.io Integration* (`hediet.vscode-drawio`).
- Create a new file `docs/diagrams/<name>.drawio.svg` and open it; the editor starts automatically.
- The file is a normal SVG, so it can be embedded in Markdown and is rendered by GitHub:
  `![Architecture](diagrams/architecture.drawio.svg)`

**Mermaid**: for small diagrams directly in Markdown (flows, sequences, states).
Rendered by GitHub and, with the extension `bierner.markdown-mermaid`, in the VS Code preview.
Syntax: <https://mermaid.js.org/intro/>

## Decisions

One file per decision: `decisions/NNNN-short-title.md`, see
[0001-pyproject.md](decisions/0001-pyproject.md) as an example.
