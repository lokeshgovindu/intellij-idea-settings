// ----------------------------------------------------------------------------

public static boolean isPrime(long n) {
    if (n == 2) return true;
    if (n < 2 || n % 2 == 0) return false;
    long sqrtOfN = (long) Math.sqrt(n);
    for (int i = 3; i <= sqrtOfN; ++i) if (n % i == 0) return false;
    return true;
}

// ----------------------------------------------------------------------------

/**
 * Check if the given number is prime or not
 */
public static boolean isPrime(long n) {
    if (n == 2) return true;
    if (n < 2 || n % 2 == 0) return false;
    long sqrtOfN = (long) Math.sqrt(n);
    for (int i = 3; i <= sqrtOfN; i += 2) if (n % i == 0) return false;
    return true;
}

/**
 * Prints a string representation of "deep contents" of a specified object
 * @param os
 */
public static void print(Object... os) {
    System.out.println(Arrays.deepToString(os));
}

/**
 * Returns a string representation of "deep contents" of a specified object
 * @param os
 */
public static String toString(Object... os) {
    return Arrays.deepToString(os);
}

public static boolean contains(int[] a, int val) {
    return IntStream.of(a).anyMatch(x -> x == val);
}

// ----------------------------------------------------------------------------


/**
 * Get the method name for a depth in call stack. <br />
 * Utility function
 * @param depth depth in the call stack (0 means current method, 1 means call method, ...)
 * @return method name
 */
public static String getMethodName(final int depth)
{
  final StackTraceElement[] ste = Thread.currentThread().getStackTrace();

  //System. out.println(ste[ste.length-depth].getClassName()+"#"+ste[ste.length-depth].getMethodName());
  // return ste[ste.length - depth].getMethodName();  //Wrong, fails for depth = 0
  return ste[ste.length - 1 - depth].getMethodName(); //Thank you Tom Tresansky
}

-------------------------------------------------------------------------------
