package tree;

import data.AttributeRequirement;

public class Node {
    private AttributeRequirement requirement;
    private Node leftChild;
    private Node rightChild;

    public AttributeRequirement getRequirement() {
        return requirement;
    }

    public void setRequirement(AttributeRequirement requirement) {
        this.requirement = requirement;
    }
}
