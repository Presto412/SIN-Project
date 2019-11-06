#include <iostream>
#include <bits/stdc++.h>
#include <omp.h>
using namespace std;
struct Node
{
    int data;
    Node *next;
    Node(int d)
    {
        data = d;
        next = NULL;
    }
};

Node **createAdjacencyListGraph(vector<vector<int>> &edges, int N)
{
    Node **head;
    head = new Node *[N]();
    for (int i = 0; i < N; i++)
    {
        head[i] = new Node(i);
    }
    for (int i = 0; i < edges.size(); i++)
    {
        int v1 = edges[i][0];
        int v2 = edges[i][1];
        if (head[v1]->next == NULL)
        {
            head[v1]->next = new Node(v2);
        }
        else
        {
            Node *temp = head[v1];
            while (temp->next != NULL)
                temp = temp->next;
            temp->next = new Node(v2);
        }
    }
    return head;
}

void displayAdjacencyListGraph(Node **head, int N)
{
    cout << "Graph Adjacency List Representation:\n";
    for (int i = 0; i < N; i++)
    {
        Node *temp = head[i];
        if (temp == NULL)
        {
            cout << "eh\n";
            continue;
        }
        while (temp->next != NULL)
        {
            cout << temp->data << "->";
            temp = temp->next;
        }
        if (temp != NULL)
            cout << temp->data << "\n";
    }
}
vector<bool> visited(8, false);
void heavyCompute(Node *x)
{
    // any compute heavy independent operation on each node here
    // that facilitates use of parallel traversal
}
void BFSAdjacencyList(Node **head, int N)
{
    cout << "Graph Traversal(BFS Queue - Popped from front, pushed from rear):\n";
    int qSize;
    queue<Node *> q;
    q.push(head[0]);
    visited[0] = true;
    while (!q.empty())
    {
        qSize = q.size();
#pragma omp parallel for
        for (int i = 0; i < qSize; i++)
        {
            Node *currNode;
#pragma omp critical
            {
                currNode = q.front();
                q.pop();
                cout << "Popped:" << currNode->data << "\n";
            }
            heavyCompute(currNode);
            while (currNode->next)
            {
#pragma omp critical
                if (!visited[currNode->next->data])
                {

                    q.push(head[currNode->next->data]);
                    visited[currNode->next->data] = true;
                    cout << "Pushed:" << currNode->next->data << "\n";
                }

                currNode = currNode->next;
            }
        }
    }
    for (int i = 0; i < visited.size(); i++)
    {
        if (visited[i])
        {
            cout << i << " is visited\n";
        }
    }
    cout << "Done.\n";
}

int main()
{
    vector<vector<int>> edges = {{0, 1}, {0, 7}, {1, 3}, {1, 4}, {2, 5}, {2, 6}, {2, 7}, {3, 1}, {4, 2}, {5, 6}, {6, 2}, {7, 2}, {7, 3}};
    int n = 8;
    Node **head = createAdjacencyListGraph(edges, n);
    displayAdjacencyListGraph(head, n);
    BFSAdjacencyList(head, n);
    // DFSAdjacencyList(head, n);
    // TopologicalSort(head, n);
    return 0;
}
