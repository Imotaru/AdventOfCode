import java.util.ArrayList;
import java.util.HashSet;
import java.util.InputMismatchException;
import java.util.Stack;

public class Day12 {
    public static long Part1() {
        return Solve(true);
    }


    public static long Part2() {
        return Solve(false);
    }

    static long Solve(boolean isPartOne) {
        ArrayList<String> lines = Helper.ReadFile(12, false);
        ArrayList<Node> nodes = new ArrayList<>();

        for (String line : lines) {
            String[] startEnd = line.split("-");
            Node node1 = TryCreateNode(startEnd[0], nodes);
            Node node2 = TryCreateNode(startEnd[1], nodes);
            node1.connectedNodes.add(node2);
            node2.connectedNodes.add(node1);
        }

        int pathAmount = GetValidPathAmount(nodes, false);
        if (isPartOne) {
            return pathAmount;
        }
        for (Node node : nodes) {
            if (node.isBig) {
                continue;
            }
            node.maxVisitAmount = 2;
            pathAmount += GetValidPathAmount(nodes, true);
            node.maxVisitAmount = 1;
        }
        return pathAmount;
    }

    static int GetValidPathAmount(ArrayList<Node> nodes, boolean onlyCountIfSmallVisitedTwice) {
        Node startNode = null;
        Node endNode = null;

        for (Node node : nodes) {
            if (startNode == null && node.nodeName.equals("start")) {
                startNode = node;
            } else if (endNode == null && node.nodeName.equals("end")) {
                endNode = node;
            }
        }

        if (startNode == null || endNode == null) {
            throw new InputMismatchException("Start or End node is missing in input");
        }

        int pathCount = 0;
        Stack<Node> nodePath = new Stack<>();
        nodePath.add(startNode);
        while (true) {
            Node currentNode = nodePath.peek();
            boolean nodeFound = false;
            if (currentNode.nodeName.equals("end")) {
//                PrintPath(nodePath);
                if (onlyCountIfSmallVisitedTwice) {
                    HashSet<Node> uniqueSmallNodes = new HashSet<>();
                    int totalSmallNodeCount = 0;
                    for (Node node : nodePath) {
                        if (node.isBig) {
                            continue;
                        }
                        uniqueSmallNodes.add(node);
                        totalSmallNodeCount++;
                    }
                    if (totalSmallNodeCount != uniqueSmallNodes.size()) {
                        pathCount++;
                    }
                } else {
                    pathCount++;
                }
            } else {
                currentNode.visitAmounts++;
                for (Node node : currentNode.connectedNodes) {
                    if (!node.CanBeVisited()) {
                        continue;
                    }
                    nodeFound = true;
                    nodePath.add(node);
                    break;
                }
            }
            if (!nodeFound) {
                while (!nodeFound) {
                    if (nodePath.size() == 1) {
                        break;
                    }
                    Node lastNode = nodePath.pop();
                    if (lastNode.visitAmounts > 0) {
                        lastNode.visitAmounts--;
                    }
                    currentNode = nodePath.peek();
                    boolean pastOldNode = false;
                    for (Node node : currentNode.connectedNodes) {
                        if (node == lastNode) {
                            pastOldNode = true;
                            continue;
                        }
                        if (!node.CanBeVisited()) {
                            continue;
                        }
                        if (pastOldNode) {
                            nodeFound = true;
                            nodePath.add(node);
                            break;
                        }
                    }
                }
            }
            if (!nodeFound) {
                break;
            }
        }

        return pathCount;
    }

    static void PrintPath(Stack<Node> path) {
        for (Node node : path) {
            System.out.print(node.nodeName + ", ");
        }
        System.out.print("\n");
    }

    static Node TryCreateNode(String nodeName, ArrayList<Node> nodes) {
        for (Node node : nodes) {
            if (node.nodeName.equals(nodeName)) {
                return node;
            }
        }
        Node node = new Node(nodeName);
        nodes.add(node);
        return node;
    }
}

class Node {
    public String nodeName;
    public boolean isBig;
    public int maxVisitAmount;
    public int visitAmounts;
    public ArrayList<Node> connectedNodes;

    public boolean CanBeVisited() {
        return isBig || visitAmounts < maxVisitAmount;
    }

    public Node(String nodeName) {
        this.nodeName = nodeName;
        isBig = Character.isUpperCase(nodeName.charAt(0));
        visitAmounts = 0;
        maxVisitAmount = 1;
        connectedNodes = new ArrayList<>();
    }
}