def sort(self):
        """
        Sort the robot's list.
        """
        # Let's start by doing some base cases
        # we can always do a bubble sort here because the robot can hold one item in hand and look at the next item and swap if it is smaller or larger
        while True:
            # while all the functions that we are going to be using return true, we will define
            # the base cases of when to break the loop
            while True:

                if self.can_move_right() == False:
                    break

                # but if it true that it can move right, we will compare the items and make the swap:
                self.swap_item()    # after swapping the item, we move to the right:

                self.move_right()   # since we set can_move_right()==False in the beginning, it will automatically break
                                    # if cannot move right. But if it is True, which is what we intended in the beginning, it will move_right()

                # then, we make the comparison between the item being held and the next item.
                # so the compare_item function takes care of it for us where if the item held is less than the
                # next item in the list, we get a return of -1 and if we compare that with 0, we see that the item
                # being held is larger than the one on the right so we make the swap

                if self.compare_item() < 0:
                    self.swap_item()

                # what's next?
                # after swapping the item, we get to the end of the list:
                # when we get to the end of the list, we need to swap the last item:

                if self.can_move_right() == False:      # when we are at the end of the list, can_move_right returns False
                    self.swap_item()                    # swap the last item as it belong in the last of the list and move on
                    break

            # then, we go to the outer loop of being while True and see what to do when it is false
            # let's say we are at the end of the list and and we cannot move right, it would also break the loop

            if self.compare_item() == None and self.can_move_right()==False:
                break

            # last thing to implement is to make sure the smallest item is at the beginning of the list;

            while True:
                self.move_left()
                # swap the smallest item:
                if self.compare_item() == None:
                    self.swap_item()
                    break

                # and after that we keep swapping the smaller items:
                # if the value of item being held is greater than the next item, compare_item returns 1
                # so we make the swap continuously to get to the list in order

                if self.compare_item() > 0:
                    self.swap_item()

            # if we cannot move right any further, that means we are already at the end so we break the loop and we are done!
            if self.move_right() == False:
                    break
