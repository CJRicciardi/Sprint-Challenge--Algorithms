#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)O(1) - constant run time.  For negative numbers it won't run even once, 'a' will go unchanged.  When 0 < n <= 1 it will run once.  When n > 1 it will only need to run twice, no matter the number.  So that's about as close to a constant runtime as things get with out actually being constant.


b) O(n^2) - quadratic runtime.  The larger n gets, the more times the while loop needs to run, and the larger n's cause the while loop to run more as well.  


c) o(n) - linear runtime.  The function runs n times.  So it's the super simple line equation x=y, where 'x' is the number of times the function runs, and 'y' is 'n'.

## Exercise II
This solution would best be solved by a binary search.  So the runtime would be O(logn) - logarithmic run time.  

The way you would go about solving this problem in a hypothetical world where eggs don't break when dropped from your hand goes as follows.  To start roof = floor n.  You would go to the floor n/2 and drop the egg.  If it breaks proceed to n/4, if not head to n3/4, and drop the egg.  If the egg breaks you always go up, and if it does not you always go down.  The slightly tricky part is the math.  So you need to keep track of bottom, top and current floor.  To start, bottom = ground level, top = n (the roof), and current = n/2 floor.  If the egg breaks, the top becomes the current floor.  If not the current floor becomes the bottom.  The equation for the next floor for the expiriment is:
 new test floor = (top - bottom) // 2.
 
 If you repeat the expirement in this manner you will break the fewest amount of eggs to find out which floor if floor f.  
 In all practicality you can probably assume f = ground level, but in this crazy world of the expirement you may waste an egg.