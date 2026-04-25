import streamlit as st
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

def bfs(start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append(path + [neighbor])

def dfs(start, goal, path=[]):
    path = path + [start]

    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in path:
            result = dfs(neighbor, goal, path)
            if result:
                return result

st.title("Smart Navigation System")

start = st.text_input("Start Node", "A")
goal = st.text_input("Goal Node", "E")

if st.button("Find Path"):
    st.write("BFS Path:", bfs(start, goal))
    st.write("DFS Path:", dfs(start, goal))