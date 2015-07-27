intro_to_python_profiling
=========================

A very brief introduction to profiling python programs

First:
------

 * Open http://docs.python.org/2/library/profile.html for reference.
 * Clone this repository by running:
   * git clone https://github.com/ggould256/intro_to_python_profiling.git
   * cd intro_to_python_profiling

Second:
-------

 * Read example.py.
 * It doesn't matter whether you see the two performance bugs that are
   not-very-hidden in there.

Third:
------

 * Run './example.py small.txt'
 * It's slow.
   * How slow?  Run 'time ./example.py small.txt'
   * 'time' is a command-line tool that is the simplest and most basic
     profiling tool.
     * Its outputs are:
       * "real" is the "wall-clock time" required to run the command
       * "user" is the time your code was doing work
       * "sys" is work the system had to do to help your code (like managing
         the computer's memory)
       * Time not accounted for there was spent waiting (like waiting for a
         network connection or a file to load off of the disk)
 * Get in the habit of running 'time' any time things seem slow.

Fourth:
-------

 * We want to know _why_ it's slow.  Time to meet cProfile.
 * Run 'python -m cProfile example.py small.txt'
 * Lots of pretty output!  Let's see what it means.
   * ncalls -- how many times a function was called.
     * If it's two numbers, the second number is how many times it was called 
       from outside of itself.
   * tottime -- how much time was spent in this function, excluding time spent
     in functions called from this function
   * cumtime -- how much time was spent in this function
 * Note that ncalls and tottime both indicate that nth_fib is stupid expensive.

Fifth:
------

 * How do we fix nth_fib?  There's a lot of ways, but the simplest is to just
   keep track of its output and not repeat ourselves.
 * Read example-cached.py
 * Run 'time ./example-cached.py small.txt'.  Much better!
 * Run 'python -m cProfile example-cached.py small.txt'
   * Note the much smaller ncalls number

Sixth:
------

 * Run 'time ./example-cached.py huge.txt'
   * This is pretty good, but we can do better.
 * Run 'python -m cProfile example-cached.py huge.txt'
   * tottime shows that "method 'readlines'" is now our hot-spot.
   * cumtime shows that nth_line is responsible for those calls.
   * Clearly nth_line is now a problem.
 * nth_line is actually pretty dumb -- we re-read the whole file for each line.

Seventh:
--------

 * Read example-cached-sane-io.py
 * Run 'time ./example-cached-sane-io.py huge.txt'
   * Nice!
 * What will we see when we run cProfile on it?
   * Expect a much smaller ncalls and tottime for "method 'readlines'"
 * Try it.  Run: 'python -m cProfile example-cached-sane-io.py huge.txt'
   * Better!
   * Further optimization is possible
     * ncalls for rstrip is unnecessarily high
   * But don't do it!
     * tottime says you could only buy back 2 milliseconds that way.

Eighth:
-------

 * Guiding principles:
   * 'time' is your first line of inquiry.  Know how long things take before 
      you start tinkering.
   * 'cProfile' gives you a ton of information.
     * For a large program, it can be overwhelming.
     * It has a million uses and options not described here.
   * Do not spend time optimizing without a clear, quantifiable benefit!
     * Optimization trades developer time for user time.  Be sure the trade
       is at a good price!
     * The value of optimizing is approximately tottime / code complexity.
   * Sometimes profiling is weird and wrong
     * The profiler itself slows your code down, leading to odd behaviour
     * The profiler can sometimes be wrong about where it attributes time
       * complex lambdas and monkey-patching can really confuse it.
