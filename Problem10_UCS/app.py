import streamlit as st
import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'D': 1},
    'D': {'F': 3},
    'E': {'F': 1},
    'F': {}
}

def ucs(start, goal):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node not in visited:
            visited.add(node)
            path = path + [node]

            if node == goal:
                return path, cost

            for neighbor in graph[node]:
                heapq.heappush(queue, (cost + graph[node][neighbor], neighbor, path))

st.title("Uniform Cost Search (UCS)")

start = st.text_input("Start Node", "A")
goal = st.text_input("Goal Node", "F")

if st.button("Find Optimal Path"):
    path, cost = ucs(start, goal)
    st.write("Optimal Path:", path)
    st.write("Total Cost:", cost)