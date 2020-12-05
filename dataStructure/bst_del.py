def min_right_subtree(self, curr):
    if curr.left_child:
        return self.min_right_subtree(curr.left_child)
    else:
        return curr

def del_val(self, key):
    self._del_val(self.root, None, None, key)

def _del_val(self, curr, prev, is_left, key):
    if curr:
        if key == curr.data:
            if curr.left_child ==None and curr.right_child == None:
                if prev:
                    if is_left == True:
                        prev.left_child = None
                    else:
                        prev.right_child = None
                else:
                    self.root = None
            elif curr.left_child and curr.right_child:
                if prev:
                    min_child = self.min_right_subtree(curr.right_child)
                    curr.data = min_child.data
                    self._del_val(curr)
                else:
                    self.root.data = curr.right_child.data
                    self.root.right_child = None
            elif curr.left_child == None:
                if prev:
                    if is_left:
                        prev.left_child = curr.right_child
                    else:
                        prev.right_child = curr.right_child
                else:
                    self.root = curr.right_child
            else:
                if prev:
                    if is_left:
                        prev.left_child = curr.left_child
                    else:
                        prev.right_child = curr.left_child
                else:
                    self.root = curr.right_child
        elif key < curr:
            _del_val(curr.left_child, curr, True, key)
        elif key > curr:
            _del_val(curr.right_child, curr, False, key)

    else:
        print('Value not found in a tree')