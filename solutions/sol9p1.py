class DoublyLinkedNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return "[{}, {}, {}]".format(self.prev.value, self.value, self.next.value)


class CircleList:
    def __init__(self):
        self.head = None
        pass

    def move_head(self, steps):
        for _ in range(abs(steps)):
            if steps >= 0:
                self.head = self.head.next
            else:
                self.head = self.head.prev

    def insert(self, value):
        """Does not move head"""
        new_node = DoublyLinkedNode(value)
        new_node.next = self.head
        new_node.prev = self.head.prev
        self.head.prev.next = new_node
        self.head.prev = new_node

    def append(self, value):
        """Does not move head"""
        new_node = DoublyLinkedNode(value)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node

    def remove_shift_left(self):
        """Removes head and sets the new head to whatever was right of the old head"""
        left = self.head.prev
        right = self.head.next
        left.next = right
        right.prev = left
        self.head = right

    def get_head_value(self):
        return self.head.value

    def __str__(self):
        vals = []
        ptr = self.head
        while True:
            vals.append(str(ptr.value))

            ptr = ptr.next
            if ptr is self.head:
                break

        return ' '.join(vals)


def solution(num_players, max_marble_score):
    circle = CircleList()
    player_scores = [0] * num_players

    circle.head = DoublyLinkedNode(0)
    circle.head.next = circle.head
    circle.head.prev = circle.head

    for i in range(max_marble_score):
        current_player_idx = i % num_players
        marble_score = i + 1

        if marble_score % 23 == 0:
            player_scores[current_player_idx] += marble_score
            circle.move_head(-7)
            player_scores[current_player_idx] += circle.get_head_value()
            circle.remove_shift_left()
        else:
            circle.move_head(1)
            circle.append(marble_score)
            circle.move_head(1)

    return max(player_scores)


def solve(input_data):
    num_players = int(input_data.split()[0])
    max_marble_score = int(input_data.split()[6])
    return solution(num_players, max_marble_score)
