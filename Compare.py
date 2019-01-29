def compare(ll1,ll2):
    x = ll1.len()
    y = ll2.len()
    ll1_current = ll1.head
    ll2_current = ll2.head
    if x == y:
        newLinkedList = LinkedList()
        for i in range(x):
            newLinkedList.add_in_tail(Node(ll1_current.value + ll2_current.value))
            ll1_current = ll1_current.next
            ll2_current = ll2_current.next
        return newLinkedList
    else:
        print("Списки не равны.")
