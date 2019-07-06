/*****************************************************************************/
/*                                                                           */
/*                  This is  Lokesh Govindu's header file.                   */
/*                                                                           */
/* - This is my C/C++ backup's header file.                                  */
/*                                                                           */
/*****************************************************************************/

/**
 * \file    LoGo.h
 *
 * \author  Lokesh Govindu
 * Contact: lokeshgovindu@gmail.com
 *
 * \brief 
 *
 * TODO:    long description
 *
 * \note
 */

#ifndef __LoGo_H__
#define __LoGo_H__

#define LGCHR(x)                        #@x
#define LGSTR_(x)                       #x
#define LGSTR(x)                        LGSTR_(x)
#define LGWSTR_(x)                      L###x
#define LGWSTR(x)                       LGWSTR_(x)
#define LGCAT(x, y)                     x##y

#ifndef _UNICODE
#define LGTSTR(str)                     LGSTR(str)
#else
#define LGTSTR(str)                     LGWSTR(str)
#endif  // _UNICODE

#pragma message("[INFO] ------------------------------------------------------------------------")
#pragma message("[INFO] *** Including [" __FILE__ "] header file ***")
#pragma message("[INFO] ------------------------------------------------------------------------")

/*****************************************************************************/

#include <tchar.h>
#include <io.h>
#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <stdarg.h>

#include <windows.h>

/*****************************************************************************/

// Constants

#define MPI                         3.14159265358979323846264338327950288419716939937510
#define LGLINE                      "---------------------------------------------------------------------------------------------------"
#define LGLINEA                     "---------------------------------------------------------------------------------------------------"
#define LGLINEW                     L"---------------------------------------------------------------------------------------------------"


// C Macros
#define LGPRINT_INT(x)              printf_s("%s = [%d]\n",     LGSTR(x), x)
#define LGPRINT_UINT(x)             printf_s("%s = [%u]\n",     LGSTR(x), x)
#define LGPRINT_FLT(x)              printf_s("%s = [%f]\n",     LGSTR(x), x)
#define LGPRINT_DBL(x)              printf_s("%s = [%lf]\n",    LGSTR(x), x)
#define LGPRINT_STR(x)              printf_s("%s = [%s]\n",     LGSTR(x), x)
#define LGPRINT_DEC(x)              printf_s("%s = [%d]\n",     LGSTR(x), x)
#define LGPRINT_HEX(x)              printf_s("%s = [%#x]\n",    LGSTR(x), x)
#define LGPRINT_OCT(x)              printf_s("%s = [%#o]\n",    LGSTR(x), x)
#define LGPRINT_PTR(x)              printf_s("%s = [%#x]\n",    LGSTR(x), x)

// Celsius(°C) / Fahrenheit(°F) Conversion
#define FTOC(f)                     ((((f) - 32.0) * 5.0) / 9.0)
#define CTOF(c)                     ((((c) * 9.0) / 5.0) + 32.0)

#define DEG_TO_RAD(deg)             ((deg * 2.0 * MPI) / 360.0)
#define RAD_TO_DEG(rad)             ((360.0 / ( 2.0 * MPI)) * rad)

#define ARRAY_SIZE(A)               (sizeof(A) / sizeof(A[0]))
#define SIZE_ARRAY(A)               (sizeof(A) / sizeof(A[0]))


/* Built-in data-types in C/C++ */

typedef signed char                 Int8;
typedef signed short                Int16;
typedef signed int                  Int32;
typedef signed long long            Int64;
typedef signed __int64              Int64;
typedef unsigned char               UInt8;
typedef unsigned short              UInt16;
typedef unsigned int                UInt32;
typedef unsigned long long          UInt64;
typedef unsigned __int64            UInt64;
typedef char                        Char;
typedef float                       Single;
typedef double                      Double;

#if !defined(__cplusplus)
typedef unsigned char               Boolean;
#if !defined(MAX_STRING_LEN)    
#define MAX_STRING_LEN              256
#endif
typedef char                        String[MAX_STRING_LEN];
#endif /* __cplusplus */

/*****************************************************************************/


#if !defined(__cplusplus)

#define FOR(i, n)                   for (int i = 0; i < (n); ++i)
#define FORR(i, n)                  for (int i = n - 1; i >= 0; --i)
#define FORN(i, x, n)               for (int i = x; i <= (n); ++i)
#define FORU(i, x, n)               for (int i = x; i <= (n); ++i)
#define FORD(i, n, x)               for (int i = n; i >= (x); --i)
#define FORX(i, a, b, inc)          for (int i = a; i <= (b); i += (inc))

#define FORI(N)                     FOR(i, N)
#define FORJ(N)                     FOR(j, N)
#define FORK(N)                     FOR(k, N)

#define FORRI(N)                    FORR(i, N)
#define FORRJ(N)                    FORR(j, N)
#define FORRK(N)                    FORR(k, N)

//-----------------------------------------------------------------------------
// C++ starts here!
//-----------------------------------------------------------------------------

#else /* __cplusplus */

// C
#include <cassert>
#include <cctype>
#include <cerrno>
#include <cfloat>
#include <ciso646>
#include <climits>
#include <clocale>
#include <cmath>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

// C++
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>

// _MSC_VER >= 1700 | VisualStudio 2012, VC++ compiler

#if _MSC_VER >= 1700 || __cplusplus >= 201103L
#include <array>
#include <atomic>
#include <chrono>
#include <codecvt>
#include <condition_variable>
#include <forward_list>
#include <future>
#include <initializer_list>
#include <mutex>
#include <random>
#include <ratio>
#include <regex>
#include <scoped_allocator>
#include <system_error>
#include <thread>
#include <tuple>
#include <typeindex>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
#endif

#if __cplusplus >= 201402L
#include <shared_mutex>
#endif

#if __cplusplus >= 201703L
#include <charconv>
#include <filesystem>
#endif

#define __LGCPP11   _MSC_VER >= 1700 || __cplusplus >= 201103L
#define __LGCPP14   _MSC_VER >= 1700 || __cplusplus >= 201402L

/*****************************************************************************/

#define LOGO_NS         LoGo
#define LOGO_NS_BEGIN   namespace LOGO_NS {
#define LOGO_NS_END     }
#define LOGO_NS_USE     using namespace LOGO_NS;

typedef bool                                    Boolean;

typedef std::vector<int>                        VI;
typedef std::vector<unsigned long>              VUL;
typedef std::vector<unsigned long long>         VULL;
typedef std::vector<double>                     VD;
typedef std::vector<std::vector<double>>        VVD;
typedef std::vector<std::vector<int>>           VVI;
typedef std::vector<Int32>                      VInt32;
typedef std::vector<UInt32>                     VUInt32;
typedef std::vector<Int64>                      VInt64;
typedef std::vector<UInt64>                     VUInt64;
typedef std::vector<long>                       VL;
typedef std::vector<unsigned long>              VUL;

typedef std::vector<std::string>                VS;
typedef std::vector<std::wstring>               VWS;
typedef std::vector<std::vector<std::string>>   VVS;
typedef std::vector<std::vector<std::wstring>>  VVWS;

// ----------------------------------------------------------------------------
// UNICODE related stuff
// ----------------------------------------------------------------------------

#ifndef _UNICODE
typedef std::string                 String;
#define tcout                       std::cout
typedef std::string                 tstring;
#else /* _UNICODE */
typedef std::wstring                String;
#define tcout                       std::wcout
typedef std::wstring                tstring;
#endif  // _UNICODE

typedef std::vector<tstring>        VTS;

/*****************************************************************************/

#define LGSCOPEDTIMER(st)           LOGO_NS::ScopedTimer st(__FUNCTION__)
#define MPI                         3.14159265358979323846264338327950288419716939937510

/*****************************************************************************/

#define SIZE(C)                     C.size()
#define ALL(C)                      (C).begin(), (C).end()
#define ARRAY_SIZE(A)               (sizeof(A) / sizeof(A[0]))
#define SIZE_ARRAY(A)               (sizeof(A) / sizeof(A[0]))
#define ALL_ARRAY(A)                (A), (A) + ARRAY_SIZE(A)
#define ARRAY_ALL(A)                (A), (A) + ARRAY_SIZE(A)

//#define FOREACH(T, it, C)         for (T::iterator it = (C).begin(); it != (C).end(); ++it)

#if __LGCPP11   /* VisualStudio 2012, VC++ compiler */
#define FOR(i, n)                   for (decltype(n) i = 0; i < (n); ++i)
#define FORR(i, n)                  for (decltype(n) i = n - 1; i >= 0; --i)
#define FORC(i, C)                  for (size_t i = 0; i < (C).size(); ++i)
#define FORN(i, x, n)               for (decltype(n) i = x; i <= (n); ++i)
#define FORU(i, x, n)               for (decltype(N) i = x; i <= (n); ++i)
#define FORD(i, n, x)               for (decltype(x) i = n; i >= (x); --i)
#define FORX(i, a, b, inc)          for (decltype(b) i = a; i <= (b); i += (inc))
#define FOREACH(x, C)               for (auto& x : C)
#else
#define FOR(i, n)                   for (int i = 0; i < (n); ++i)
#define FORR(i, n)                  for (int i = n - 1; i >= 0; --i)
#define FORC(i, C)                  for (int i = 0; i < (C).size(); ++i)
#define FORN(i, x, n)               for (int i = x; i <= (n); ++i)
#define FORU(i, x, n)               for (int i = x; i <= (n); ++i)
#define FORD(i, n, x)               for (int i = n; i >= (x); --i)
#define FORX(i, a, b, inc)          for (int i = a; i <= (b); i += (inc))
#define FOREACH(T, it, C)           for (T::iterator it = (C).begin(); it != (C).end(); ++it)
#endif

#define FORI(N)                     FOR(i, N)
#define FORJ(N)                     FOR(j, N)
#define FORK(N)                     FOR(k, N)

#define FORCI(C)                    FORC(i, C)
#define FORCJ(C)                    FORC(j, C)
#define FORCK(C)                    FORC(k, C)

#define FORRI(N)                    FORR(i, N)
#define FORRJ(N)                    FORR(j, N)
#define FORRK(N)                    FORR(k, N)


#define TIME(t)                     clock_t t = clock()
#define TIME_DIFF(t1, t2)           (1.0 * abs(t2 - t1) / CLOCKS_PER_SEC)

#define SORT(C)                     sort(ALL(C))
#define FIND(c, v)                  (find(c.begin(), c.end(), v) != c.end())
#define SWAP(x, y)                  (x) ^= (y) ^= (x) ^= (y)

#define LGPRINT_LINE                cout << LGLINE << endl
#define LGPRINT_CRLF                cout << endl

#define READ_NUMBER(num)            cin >> num;
#define READ_STRING(S)              \
    cin.ignore();                   \
    getline(cin, S);

#define LGTRACE(a)              std::cout << (a) << std::endl
#define LGTRACE(a)              std::cout << (a) << std::endl
#define LGTRACE_FUNC            std::cout << "Function : " << (__FUNCTION__) << std::endl
#define LGTRACE_FUNCSIG         std::cout << "FuncSign : " << (__FUNCSIG__) << std::endl

#define LGTRACE1(a)             std::cout << (a) << std::endl

#define LGTRACE2(a, b)                                                      \
    std::cout << (a) << ", " << (b) << std::endl

#define LGTRACE3(a, b, c)                                                   \
    std::cout << (a) << ", " << (b) << ", " << (c) << std::endl

#define LGTRACE4(a, b, c, d)                                                \
    std::cout << (a) << ", " << (b) << ", " << (c) << ", " << (d) << std::endl

#define LGTRACE5(a, b, c, d, e)                                             \
    std::cout << (a) << ", " << (b) << ", " << (c) << ", " << (d) << ", "   \
              << (e) << std::endl

#define LGTRACE6(a, b, c, d, e, f)                                          \
    std::cout << (a) << ", " << (b) << ", " << (c) << ", " << (d) << ", "   \
              << (e) << ", " << (f) << std::endl

#define LGTRACE7(a, b, c, d, e, f, g)                                       \
    std::cout << (a) << ", " << (b) << ", " << (c) << ", " << (d) << ", "   \
              << (e) << ", " << (f) << ", " << (g) << std::endl

#define LGTRACE8(a, b, c, d, e, f, g, h)                                    \
    std::cout << (a) << ", " << (b) << ", " << (c) << ", " << (d) << ", "   \
              << (e) << ", " << (f) << ", " << (g) << ", " << (h) << std::endl

#define LGTRACE9(a, b, c, d, e, f, g, h, i)                                 \
    std::cout << (a) << ", " << (b) << ", " << (c) << ", " << (d) << ", "   \
              << (e) << ", " << (f) << ", " << (g) << ", " << (h) << ", "   \
              << (i) << std::endl

#define LGPRINT_FMT(x)  LGSTR(x) " = [" << (x) << "]"
#define LGPRINT_SEP     ", "

#define LGPRINT(x)  std::cout << LGPRINT_FMT(x) << std::endl
#define LGPRINT1(x) std::cout << LGPRINT_FMT(x) << std::endl

#define LGPRINT2(a, b)                                                      \
    std::cout                                                               \
        << LGPRINT_FMT(a) << LGPRINT_SEP                                    \
        << LGPRINT_FMT(b) << std::endl

#define LGPRINT3(a, b, c)                                                   \
    std::cout                                                               \
        << LGPRINT_FMT(a) << LGPRINT_SEP                                    \
        << LGPRINT_FMT(b) << LGPRINT_SEP                                    \
        << LGPRINT_FMT(c) << std::endl

#define LGPRINT4(a, b, c, d)                                                \
    std::cout                                                               \
        << LGPRINT_FMT(a) << LGPRINT_SEP                                    \
        << LGPRINT_FMT(b) << LGPRINT_SEP                                    \
        << LGPRINT_FMT(c) << LGPRINT_SEP                                    \
        << LGPRINT_FMT(d) << std::endl

#define LGPRINT5(a, b, c, d, e)                                             \
    std::cout                                                               \
        << LGPRINT_FMT(a) << LGPRINT_SEP                                    \
        << LGPRINT_FMT(b) << LGPRINT_SEP                                    \
        << LGPRINT_FMT(c) << LGPRINT_SEP                                    \
        << LGPRINT_FMT(d) << LGPRINT_SEP                                    \
        << LGPRINT_FMT(e) << std::endl

/*****************************************************************************/

//
// Open file for reading
//
#define LGFILE_OPEN(fs, path)                           \
    fstream fs(path);                                   \
    if (fs.is_open() == false) {                        \
        std::cout << "file not opened" << std::endl;    \
    }


//
// Redirect stdout to a text file.
//
#define LGREDIRECTSTDOUT(filePath)                                          \
    printf_s("Redirecting stdout to [%s], @ Func : [%s], Line : [%d]\n",    \
        filePath, __FUNCTION__, __LINE__);                                  \
    freopen_s((FILE**)stdout, filePath, "w+t", stdout);

//
// Redirect stdin to a text file.
//
#define LGREDIRECTSTDIN(filePath)                                           \
    printf_s("Redirecting stdin to [%s], @ Func : [%s], Line : [%d]\n",     \
        filePath, __FUNCTION__, __LINE__);                                  \
    freopen_s((FILE**)stdin, filePath, "r", stdin);

//
// Redirect stdout back to console.
//
#define LGREDIRECTSTDOUTTOCONSOLE                                           \
    freopen_s((FILE**)stdout, "con", "w", stdout);                          \
    printf_s("Redirecting stdout to [CON], @ Func : [%s], Line : [%d]\n",   \
        __FUNCTION__, __LINE__);

#ifndef _LGPRINT_TIME_
#define _LGPRINT_TIME_
#define LGPRINT_TIME(exp)                                                   \
{                                                                           \
    TIME(t1);                                                               \
    exp;                                                                    \
    TIME(t2);                                                               \
    std::cout << LGSTR(exp) << " : " << TIME_DIFF(t1, t2) << " s" <<        \
    std::endl;     \
}
#endif


#define LGTRYCATCH(expression)                                              \
    try {                                                                   \
        expression;                                                         \
    }                                                                       \
    catch(std::exception& ex) {                                             \
        printf_s("Exception @ Func: %s, Line: %d : %s\n",                   \
            __FUNCTION__, __LINE__, ex.what());                             \
    }


LOGO_NS_BEGIN

//
// :::Globals
// 
const std::string VOWELS_L = "aeiou";
const std::string CONSONANTS_L = "bcdfghjklmnpqrstvwxyz";

const std::string VOWELS_U = "AEIOU";
const std::string CONSONANTS_U = "BCDFGHJKLMNPQRSTVWXYZ";

//
// :::Declarations
// 
/*****************************************************************************/
/*                         Function Declarations                             */
/*****************************************************************************/

template<typename T> std::string GetTypeName (const T& obj);
template<typename T> std::string GetClassName(const T& obj);

static std::ostream& operator << (std::ostream& out, const std::wstring& wstr);
static std::ostream& operator << (std::ostream& out, const wchar_t* wstr);

template<typename T> std::ostream& operator << (std::ostream& out, const std::vector<T>& V);
#ifndef LGDONOTUSEQUOTESFORSTRINGS
template<>    static std::ostream& operator << (std::ostream& out, const std::vector<std::string>& V);
#endif // LGDONOTUSEQUOTESFORSTRINGS

template<typename T> std::ostream& operator << (std::ostream& out, const std::set<T>& st);

template<typename T1, typename T2> std::ostream& operator << (std::ostream& out, const std::pair<T1, T2>& pr);
template<typename T1, typename T2> std::ostream& operator << (std::ostream& out, const std::map<T1, T2>& mp);

template<class T> void UNQ(T& x);

//
// :::Numbers / :::Numeric
//

static bool IsLeap(Int32 y);

template<typename T> int Sign(T val);
static int Sign(const char* szVal);
static int Sign(const std::string& val);

template<typename T> T Reverse(T N);
template<typename T> bool HasAllOddDigits(T n);
template<typename T> bool HasAllEvenDigits(T n);

static bool IsNumber(const std::string& s);

template<typename T> int BitCount(T n);
template<typename T> int BinaryCardinality(T n);
template<typename T> int DigitCount(T N);

static int numcmp(const std::string& a, const std::string& b);
static std::string Sum(std::string x, std::string y);
static std::string Sub(std::string x, std::string y);
template<typename T> bool IsPandigital(const T& N);
static bool IsPandigital(const std::string& s, int begin = 0, int end = -1);
static bool IsPandigital(const char* s);

static bool ASubsetOfB(unsigned int A, unsigned int B);
template<typename T> T Factorial(const T& n);
template<typename T> T NCR(T n, T r);
template<typename T> bool IsBouncy(T n);
template<typename T> bool IsIncreasingNumber(T n);
template<typename T> bool IsStrictlyIncreasingNumber(T n);
template<typename T> bool IsDecreasingNumber(T n);
template<typename T> bool IsStrictlyDecreasingNumber(T n);
template<typename T> T NCR(int N, int R);
template<typename T> int GetNumberOfDigits(T N);
template<typename T> T GCD(const T& a, const T& b);
template<> UInt64 GCD(const UInt64& a, const UInt64& b);
//template<> UInt64 GCD(const UInt64& a, const UInt64& b);
template<typename T> T LCM(const T& a, const T& b);
template<typename T> int GetDigitsSum(T N);
static int GetDigitsSum(const std::string& S);
template<typename T> std::string ToRadix(T value, int radix);

template<typename T> void GetPrimeFactors(T n, std::map<int, int>& mp);
template<typename T> std::vector<T> GetPrimeFactors(T n, bool duplicates = false);
template<typename T> unsigned long GetPrimeFactorsCount(T n, bool duplicates = false);
template<typename T> std::vector<T> GetAllFactors(T n);
template<typename T> int GetAllFactorsCount(T n);
template<typename T> bool IsPrime(T n);
template<typename T> std::vector<unsigned long> GetPrimes(T N);
static int CountRectangles(int W, int H, bool includeSquares = false);
template <typename T> bool IsPalindrome(T n);
template <typename T> T GetCoinChanges(const std::vector<T>& vi, T n);

//
// :::~numeric
//

//
// :::Strings
//

template<typename T> T ToLower(T s);
template<typename T> T ToUpper(T s);

static std::string ReplaceALL(std::string s, const std::string& fnd, const std::string& rep = "");
static std::string RemoveALL(const std::string& str, const std::string& seps);

static std::string GetCurrentDateTimeA();
static std::wstring GetCurrentDateTimeW();

#ifdef UNICODE
#define GetCurrentDateTime  GetCurrentDateTimeW
#else
#define GetCurrentDateTime  GetCurrentDateTimeA
#endif // !UNICODE

static char* Trim(char* s);

static std::string Trim  (const std::string& str, const std::string& seps = " \t");
static std::string TrimLeft (const std::string& str, const std::string& seps = " \t");
static std::string TrimRight(const std::string& str, const std::string& seps = " \t");

template<typename T> T ToVal(const std::string& s);
template<typename T> std::string ToString(T x);
template<typename T> std::string ToBinary(T N);
template<typename Target, typename Source> Target Convert(const Source& arg);

template<typename T> std::vector<T> Split(const std::string& s, const std::string& seps = " \t");
static std::vector<std::string> Split(const std::string& s, const std::string& seps = " \t");

template<typename T> std::stringstream& operator >> (std::stringstream& ss, std::vector<T>& v);
template<typename T> std::fstream&      operator >> (std::fstream& fs, std::vector<T>& v);

static bool IsPrefix(const std::string& s, const std::string& prefix);
static bool IsSuffix(const std::string& s, const std::string& suffix);

static bool ASubsetOfB(const std::string& A, const std::string& B);

static bool IsPalindrome(const std::string& s);
static bool IsPalindrome(const std::string& s, int l, int r);

static std::string LCSubString(const std::string& X, const std::string& Y);

// 
// :::~strings
// 

//
// :::Algorithms
//

static std::vector<std::pair<int, int>> SpanningTree_Prims(std::vector<std::vector<int>> a);
static std::vector<std::pair<int, int>> SpanningTree_Kruskals(std::vector<std::vector<int>> a);

//
// :::~Algorithms
//


template<typename T>
std::string GetTypeName(const T& obj);

/**
 * Return the type of object.
 *
 * GetTypeName(24)      => [int]
 * GetTypeName(24.9)    => [double]
 * GetTypeName('x')     => [char]
 * GetTypeName("LoGo")  => [char const [5]]
 * 
 * char* szName = "LoGo";
 * GetTypeName(szName)  => [char *]
 * 
 * struct tagStudent { };
 * GetTypeName(new tagStudent)  => [struct tagStudent *]
 * GetTypeName(tagStudent())    => [struct tagStudent]
 * 
 * class tagStudent { };
 * GetTypeName(new tagStudent)  => [class tagStudent *]
 * GetTypeName(tagStudent())    => [class tagStudent]
 * 
 * \param[in]   obj     Object
 */
template<typename T>
std::string GetTypeName(const T& obj) {
    const std::type_info& ti = typeid(obj);
    return ti.name();
}


/**
 * Return the type of object.
 *
 * GetTypeName(24)     => [int]
 * GetTypeName(24.9)   => [double]
 * GetTypeName('x')    => [char]
 * GetTypeName("LoGo") => [char const [5]]
 * 
 * char* szName = "LoGo";
 * GetTypeName(szName) => [char *]

 * struct/class tagStudent { };
 * GetClassName(new tagStudent) => [tagStudent *]
 * GetClassName(tagStudent())   => [tagStudent]
 *
 * \param[in]   obj     Object
 */
template<typename T>
std::string GetClassName(const T& obj) {
    std::string name = GetTypeName(obj);
    if (name.find("struct") == 0 || name.find("class") == 0) {
        return name.substr(name.find(' ') + 1);
    }
    return "";
}

/**
 * TODO:
 * Only because of this operator << overload function, the below statements
 * works fine.
 * 
 * std::wstring name = L"Lokesh Govindu";
 * std::cout << name << endl;
 * std::cout << name.c_str() << endl;
 */
std::ostream& operator << (std::ostream& out, const std::wstring& wstr)
{
    std::wcout << wstr;
    return out;
}

std::ostream& operator << (std::ostream& out, const wchar_t* wstr)
{
    std::wcout << wstr;
    return out;
}

/**
 * Print initializer_list elements on stdout.
 */
template<typename T>
std::ostream& operator << (std::ostream& out, const std::initializer_list<T>& il) {
    if (il.size() == 0) return out;
    auto it = il.begin();
    out << "{ " << *it;
    for (++it; it != il.end(); ++it) out << ", " << *it;
    out << " }";
    return out;
}

/**
 * Print vector elements on stdout.
 */
template<typename T>
std::ostream& operator << (std::ostream& out, const std::vector<T>& V) {
    if (V.empty()) return out;
    out << "{ " << V[0];
    for (size_t i = 1; i < V.size(); ++i) out << ", " << V[i];
    out << " }";
    return out;
}

//template<typename T>
//std::ostream& operator << (std::ostream& out, const std::vector<std::vector<T>>& VV) {
//  if (VV.empty()) return out;
//  out << "{" << std::endl;
//  for (size_t i = 0; i < VV.size(); ++i)
//      out << "    " << VV[i] << "," << std::endl;
//  out << "}";
//  return out;
//}

template<typename T>
std::ostream& operator << (std::ostream& out, const std::vector<std::vector<T>>& vv) {
    if (vv.empty()) return out;
    int R = vv.size();
    int C = vv[0].size();
    printf("\n");
    printf("    |");
    for (int i = 0; i < C; ++i) printf("%5d", i);
    printf("\n");
    out << std::string(80, '-') << std::endl;
    for (int r = 0; r < R; ++r) {
        printf("%3d |", r);
        for (int c = 0; c < C; ++c) {
            printf("%5d", vv[r][c]);
        }
        printf("\n");
    }
    return out;
}

#ifndef LGDONOTUSEQUOTESFORSTRINGS
/**
 * template specialization for std::vector<std::string>.
 * Print vector elements on stdout.
 */
template<>
static std::ostream& operator << (std::ostream& out, const std::vector<std::string>& V) {
    if (V.empty()) return out;
    out << "{ " << "\"" << V[0] << "\"";
    for (size_t i = 1; i < V.size(); ++i) {
        out << ", " << "\"" << V[i] << "\"";
    }
    out << " }";
    return out;
}
#endif // LGDONOTUSEQUOTESFORSTRINGS


template<typename T>
std::ostream& operator << (std::ostream& out, const std::set<T>& st)
{
    if (st.empty()) return out;
    set<T>::iterator it = st.begin();
    out << "{ " << *it;
    for (++it; it != st.end(); ++it) {
        out << ", " << *it;
    }
    out << " }";
    return out;
}



/**
 * Print std::pair<T1, T2> on stdout as shown below.
 * 
 * std::pair<int, int> pt = make_pair<int, int>(24, 9);
 * cout << pt << std::endl;
 * 
 * Output: (24, 9)
 */
template<typename T1, typename T2>
std::ostream& operator << (std::ostream& out, const std::pair<T1, T2>& pr) {
    out << "(" << pr.first << ", " << pr.second << ")";
    return out;
}


/**
 * \brief Print std::map elements on stdout as shown below.
 * 
 * mp = [{ (0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25) }]
 * mp = [{ 0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25 }]
 */
template<typename TKey, typename TValue>
std::ostream& operator << (std::ostream& out, const std::map<TKey, TValue>& mp)
{
    if (mp.empty()) return out;
    std::map<TKey, TValue>::const_iterator it = mp.begin();
#if 1
    out << "{ " << it->first << ": " << it->second;
    for (++it; it != mp.end(); ++it) out << ", " << it->first << ": " << it->second;
    out << " }";
#else
    out << "{ " << *it;
    for (++it; it != mp.end(); ++it) out << ", " << *it;
    out << " }";
#endif
    return out;
}


/**
 * \brief Print std::map elements on stdout as shown below.
 * 
 * mp = [{ (0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25) }]
 * mp = [{ 0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25 }]
 */
template<typename TKey, typename TValue>
std::ostream& operator << (std::ostream& out, const std::unordered_map<TKey, TValue>& mp)
{
    if (mp.empty()) return out;
    std::unordered_map<TKey, TValue>::const_iterator it = mp.begin();
#if 1
    out << "{ " << it->first << ": " << it->second;
    for (++it; it != mp.end(); ++it) out << ", " << it->first << ": " << it->second;
    out << " }";
#else
    out << "{ " << *it;
    for (++it; it != mp.end(); ++it) out << ", " << *it;
    out << " }";
#endif
    return out;
}

/**
 * \brief Converts any object (that can be convertible) to string format.
 * Here, convertible means: If '<<' operator found which can take right-hand
 * operand of type T then it can convert the object of type T to string.
 */
template<class T>
std::string ToString(T x)
{
    std::stringstream ss;
    ss << x;
    return ss.str();
}


/**
 * Converts to the requested type (which can be taken a left-hand operant of
 * type std::istringstream) from string.
 */
template<class T>
T ToVal(const std::string& s)
{
    T ret;
    std::stringstream iss(s);
    iss >> ret;
    return ret;
}


/**
 *  \brief Convert one type to another
 *  
 *  \param [in] arg Source argument
 *  
 *  \return Convert the given \a arg to the requested type
 *  
 *  \sa template<class T> T ToVal(const std::string& s)
 *  \sa template<class T> std::string ToString(T x)
 *  
 *  \code
 *  LGPRINT(Convert<std::string>(9.24));
 *  LGPRINT(Convert<double>("9.24"));
 *  LGPRINT(Convert<long>(924));
 *  LGPRINT(Convert<char>(924));
 *  
 *  Output:
 *  Convert<std::string>(9.24) = [9.24]
 *  Convert<double>("9.24") = [9.24]
 *  Convert<long>(924) = [924]
 *  Convert<char>(924) = [9]
 *  \endcode
 */
template<typename Target, typename Source>
Target Convert(const Source& arg)
{
    std::stringstream ss;
    Target ret;
    ss << arg;
    ss >> ret;
    return ret;
}


/**
 * Convert given to binary and returns in a string.
 */
template<class T>
std::string ToBinary(T N)
{
    std::string ret;
    while (N > 0) {
        ret = (N & 1 ? '1' : '0') + ret;
        N = N >> 1;
    }
    return ret;
}


/**
 * Checks for leap year.
 */
bool IsLeap(Int32 y) { return ((y % 4 == 0 && y % 100 != 0) || (y % 400 == 0)); }


/**
 *  Splits and returns the request type of std::vector.
 */
template<typename T>
std::vector<T> Split(const std::string& s, const std::string& seps)
{
    std::vector<T> ret; T val;
    for (size_t p = 0, q; p != std::string::npos; p = q) {
        p = s.find_first_not_of(seps, p);
        if (p == std::string::npos) break;
        q = s.find_first_of(seps, p);
        std::istringstream iss(s.substr(p, q - p));
        iss >> val;
        ret.push_back(val);
    }
    return ret;
}



/**
 *  \brief Splits the string into vector of strings.
 */
std::vector<std::string> Split(const std::string& s, const std::string& seps)
{
    std::vector<std::string> ret;
    for (size_t p = 0, q; p != std::string::npos; p = q) {
        p = s.find_first_not_of(seps, p);
        if (p == std::string::npos) break;
        q = s.find_first_of(seps, p);
        ret.push_back(s.substr(p, q - p));
    }
    return ret;
}



/**
 *  \brief This is almost similar to Split method, but separator is space here.
 *  
 *  Extracts vector of type T from string stream.
 */
template <typename T>
std::stringstream& operator >> (std::stringstream& ss, std::vector<T>& v)
{
    v.clear();
    T val;
    while (ss >> val) { v.push_back(val); }
    return ss;
}


/**
 *  \brief Read and returns the vector of elements from fstream (file, single line).
 */
template <typename T>
std::fstream& operator >> (std::fstream& fs, std::vector<T>& v)
{
    v.clear();

    std::string line;
    std::getline(fs, line);

    // just return if line is empty.
    size_t p = line.find_first_not_of(" ", 0);
    if (p == std::string::npos) return fs;
    size_t q = line.find_last_not_of(" ");

    line = line.substr(p, q - p + 1);
    std::stringstream ss(line);
    T val;
    while (ss >> val) { v.push_back(val); }
    return fs;
}


/**
 *  \brief Returns the prime factors and their count in std::map.
 *  
 *  \param[in]  n   Number, for which you want to get primes.
 *  \param[out] mp  Map container for storing primes and their count.
 *  
 *  \sa std::vector<T> GetPrimeFactors(T n, bool duplicates=false)
 *  
 *  \code
 *  std::map<int, int> mp;
 *  GetPrimeFactors(36, mp);
 *  LGPRINT(mp);
 *
 *  Output: mp = [{ 2: 2, 3: 2 }]
 *  \endcode
 */
template<typename T>
void GetPrimeFactors(T n, std::map<int, int>& mp)
{
    mp.clear();
    int sqrtOfN = static_cast<int>(sqrt((double)n));
    for (T x = 2; x <= sqrtOfN; ++x) {
        while (n % x == 0) {
            mp[x]++;
            n /= x;
        }
    }
    if (n != 1) mp[n]++;
}


/**
 *  \brief This function computes the prime factors of given number \a n.
 *  
 *  \param[in]  n           Number, for which you want to get prime factors.
 *  \param[in]  duplicates  Allow duplicates in output vector.
 *  
 *  \return Returns the vector of prime factors for the given number \a n.
 *  
 *  \sa void GetPrimeFactors(T n, std::map<int, int>& mp)
 *  
 *  \code
 *  GetPrimeFactors(36, true)  => [{ 2, 2, 3, 3 }]
 *  GetPrimeFactors(36, false) => [{ 2, 3 }]
 *  \endcode
 */
template<typename T>
std::vector<T> GetPrimeFactors(T n, bool duplicates)
{
    std::vector<T> ret;
    T sqrtOfN = static_cast<T>(sqrt((double)n));
    for (T x = 2; x <= sqrtOfN; ++x) {
        if (duplicates) {
            while (n % x == 0) {
                ret.push_back(x);
                n /= x;
            }
        }
        else {
            if (n % x == 0) { ret.push_back(x); }
            while (n % x == 0) { n /= x; }
        }
    }
    if (n != 1) ret.push_back(n);
    return ret;
}


/**
 *  \brief Returns the all prime factors count of a given number.
 *  
 *  \param[in]  n           Number to which you want to get the prime factors count.
 *  \param[in]  duplicates  Count duplicates also.
 *  
 *  \return     Return the prime factors count of a given number.
 *  
 *  \sa void GetPrimeFactors(T n, std::map<int, int>& mp)
 *  \sa std::vector<T> GetPrimeFactors(T n, bool duplicates=false)
 *
 *  \code
 *  GetPrimeFactorsCount(36, true)  => [4]
 *  GetPrimeFactorsCount(36, false) => [2]
 *  \endcode
 */
template<typename T>
unsigned long GetPrimeFactorsCount(T n, bool duplicates)
{
    unsigned long ret = 0;
    T sqrtOfN = static_cast<T>(sqrt((double)n));
    for (T x = 2; x <= sqrtOfN; ++x) {
        if (duplicates) {
            while (n % x == 0) {
                ++ret;
                n /= x;
            }
        }
        else {
            if (n % x == 0) { ++ret; }
            while (n % x == 0) { n /= x; }
        }
    }
    if (n != 1) ++ret;
    return ret;
}


/**
 *  \brief Returns the factors of a given number in std::vector.
 *  
 *  \param[in]  n   Number for which you want to get the factors.
 *  
 *  \return     Returns the factors of a given number \a n in std::vector.
 *  
 *  \code
 *  GetAllFactors(36) => { 1, 36, 2, 18, 3, 12, 4, 9, 6 }
 *  \endcode
 */
template<typename T>
std::vector<T> GetAllFactors(T n)
{
    std::vector<T> ret;
    T sqrtOfN = static_cast<T>(sqrt((double)n));

    ret.push_back(1);
    ret.push_back(n);
    for (T x = 2; x <= sqrtOfN; ++x) {
        if (n % x == 0) {
            ret.push_back(x);
            ret.push_back(n / x);
        }
    }

    if (sqrtOfN * sqrtOfN == n) {
        ret.pop_back();
    }

    return ret;
}


/**
 *  \brief Returns the number of factors of a given number.
 *  
 *  \param[in]  n   Number for which you want to get the factors.
 *  
 *  \return     Returns the number of factors of a given number \a n.
 *  
 *  \sa std::vector<T> GetAllFactors(T n)
 *  
 *  \code
 *  GetAllFactorsCount(36) => 9
 *  \endcode
 */
template<typename T>
int GetAllFactorsCount(T n)
{
    if (n == 1) return 1;
    int ret = 2;

    T sqrtOfN = static_cast<T>(sqrt((double)n));
    for (T x = 2; x <= sqrtOfN; ++x) {
        if (n % x == 0) {
            ret += 2;
        }
    }
    if (sqrtOfN * sqrtOfN == n) --ret;

    return ret;
}


/**
 *  \brief Checks if the given number if prime or not.
 *  
 *  \param[in]  n   Number

 *  \return True if given number \a n is prime, false otherwise.
 *  
 *  \sa std::vector<unsigned long> GetPrimes(T N)
 */
template<typename T>
bool IsPrime(T n)
{
    if (n == 2)                 return true;
    if (n <= 1 || n % 2 == 0)   return false;
    T sqrt_n = static_cast<T>(sqrt(1.0 * n));
    for (T i = 3; i <= sqrt_n; i += 2) if (n % i == 0) return false;
    return true;
}


/**
 *  \brief Computes the primes below \a N
 *  
 *  \param[in]  N   Number
 *  
 *  \return Number of primes below \a N in a vector.
 *  
 *  \sa bool IsPrime(T n)
 *  
 *  \ref http://code.activestate.com/recipes/576559-fast-prime-generator/
 */
template <typename T>
std::vector<unsigned long> GetPrimes(T N)
{
    std::vector<unsigned long> primes;
    char* sieve = new char[N / 16 + 1];
    memset(sieve, 0xFF, (N / 16 + 1) * sizeof(char));
    if (N >= 2) {
        primes.push_back(2);
    }
    for (unsigned long x = 3; x <= N; x += 2) {
        if (sieve[x / 16] & (0x01 << ((x / 2) % 8))) {
            primes.push_back(x);
            // Is prime. Mark multiplicatives.
            for (unsigned long j = 3 * x, xx = x + x; j <= N; j += xx) {
                sieve[j / 16] &= ~(0x01 << ((j / 2) % 8));
            }
        }
    }
    delete[] sieve;
    return primes;
}


int CountRectangles(int W, int H, bool includeSquares) {
    int ret = 0;
    FORN(w, 1, W) FORN(h, 1, H) {
        if (!includeSquares && w == h) continue;
        ret += (W - w + 1) * (H - h + 1);
    }
    return ret;
}


template <typename T>
struct Point2D
{
    T X, Y;
    Point2D(const T& _x = 0, const T& _y = 0) : X(_x), Y(_y) {};
    void Print() { std::cout << "(" << X << "," << Y << ")"; }
};


template <typename T>
std::ostream& operator << (std::ostream& out, const Point2D<T>& pt) {
    out << "(" << pt.X << "," << pt.Y << ")";
    return out;
}

typedef Point2D<double> fPoint2D;

static double sign(const fPoint2D& p1, const fPoint2D& p2, const fPoint2D& p3)
{
    return (p1.X - p3.X) * (p2.Y - p3.Y) - (p2.X - p3.X) * (p1.Y - p3.Y);
}

static bool PointInTriangle(const fPoint2D& pt, const fPoint2D& v1, const fPoint2D& v2, const fPoint2D& v3)
{
    bool b1, b2, b3;

    b1 = sign(pt, v1, v2) < 0.0f;
    b2 = sign(pt, v2, v3) < 0.0f;
    b3 = sign(pt, v3, v1) < 0.0f;

    return ((b1 == b2) && (b2 == b3));
}


/**
 *  \brief Compute the reverse of given number \a N
 *  
 *  \return Reverse of the given number \a N
 */
template<typename T>
T Reverse(T N)
{
    T ret = 0;
    while (N > 0) {
        ret = ret * 10 + (N % 10);
        N /= 10;
    }
    return ret;
}


//
// Returns true if all digits are odd.
// 
template<typename T> bool HasAllOddDigits(T n)
{
    for (; n > 0; n /= 10) {
        if (!(n & 1)) {
            return false;
        }
    }
    return true;
}


//
// Returns true if all digits are even.
// 
template<typename T> bool HasAllEvenDigits(T n)
{
    for (; n > 0; n /= 10) {
        if (n & 1) {
            return false;
        }
    }
    return true;
}

/**
 *  \brief Compares the given two number strings \a a and \a b
 *  
 *  \param [in] a First String
 *  \param [in] b Second String
 *  
 *  \return Comparision result of given two number strings.
 *          Returns:
 *              < 0 => a is less than b
 *              0   => a is equal to b
 *              > 0 => a is greater than b
 */
int numcmp(const std::string& a, const std::string& b)
{
    std::string sa = LOGO_NS::TrimLeft(a, "0");
    std::string sb = LOGO_NS::TrimLeft(b, "0");

    if (sa == sb) { return 0; }

    if (sa.size() < sb.size()) return -1;
    if (sa.size() > sb.size()) return 1;

    for (size_t i = 0; i < sa.size(); ++i) {
        if (sa[i] != sb[i]) {
            return sa[i] < sb[i] ? -1 : 1;
        }
    }

    return 0;
}


//
// Returns the sum of x and y
//
std::string Sum(std::string x, std::string y)
{
    using std::max;
    std::string ret;
    int         carry = 0;
    int         sum;
    size_t      len;

    // Trim leading spaces
    x = LOGO_NS::TrimLeft(x, "0");
    y = LOGO_NS::TrimLeft(y, "0");

    if (x.empty()) x = "0";
    if (y.empty()) y = "0";

    // Invoke subtract function if the given number is -ve.
    if (x[0] == '-' && y[0] == '-') {
        ret = Sum(x.substr(1), y.substr(1));
        return ret == "0" ? ret : "-" + ret;
    }
    else if (x[0] == '-') {
        return Sub(y, x.substr(1));
    }
    else if (y[0] == '-') {
        return Sub(x, y.substr(1));
    }

    len = max(x.size(), y.size());

    if (x.size() < len) x.insert(0, std::string(len - x.size(), '0'));
    if (y.size() < len) y.insert(0, std::string(len - y.size(), '0'));
    ret.resize(len);

    for (int i = (int) (len - 1); i >= 0; --i) {
        // Convert char to int using: ch & 0xf
        sum     = (x[i] & 0xf) + (y[i] & 0xf) + carry;
        carry   = (sum > 9 ? 1 : 0);
        sum     = sum % 10;
        ret[i]  = sum | 0x30;   // Convert digit to char
    }

    if (carry) ret.insert(ret.begin(), '1');

    return ret;
}


/**
 *  \brief Computes the subtraction of two number strings.
 *  
 *  \param [in] x First number
 *  \param [in] y Second number
 *  \return Subtraction result of x and y
 *  
 *  \details Details
 */
std::string Sub(std::string x, std::string y)
{
    using std::max;
    bool        minusSign = false;
    std::string ret;
    int         carry = 0;

    // Trim leading spaces
    x = LOGO_NS::TrimLeft(x, "0");
    y = LOGO_NS::TrimLeft(y, "0");

    if (x.empty()) x = "0";
    if (y.empty()) y = "0";

    // Invoke sum function if the given number is -ve.
    if (x[0] == '-' && y[0] == '-') {
        return Sub(y.substr(1), x.substr(1));
    }
    else if (x[0] == '-') {
        ret = Sum(x.substr(1), y);
        return ret == "0" ? ret : "-" + ret;
    }
    else if (y[0] == '-') {
        return Sum(x, y.substr(1));
    }

    int cmp = numcmp(x, y);

    if (cmp == 0) {
        return "0";
    }
    else if (cmp < 0) {
        std::swap(x, y);
        minusSign = true;
    }

    size_t len = max(x.size(), y.size());
    if (x.size() < len) x.insert(0, std::string(len - x.size(), '0'));
    if (y.size() < len) y.insert(0, std::string(len - y.size(), '0'));
    ret.resize(len);

    for (int i = (int) (len - 1); i >= 0; --i) {
        // Convert char to int using: ch & 0xf
        int sum = (x[i] & 0xf) - (y[i] & 0xf) + carry;
        if (sum < 0) { carry = -1; sum += 10; }
        else         { carry = 0; }
        sum = sum % 10;
        ret[i] = sum | 0x30;    // Convert digit to char
    }

    // Remove leading zeros (007)
    ret = LOGO_NS::TrimLeft(ret, "0");
    if (ret.empty()) return "0";

    if (minusSign) ret.insert(ret.begin(), '-');
    return ret;
}

//
// Contain all the digits 1 to 9, but not necessarily in order.
// 
template<typename T> bool IsPandigital(const T& N)
{
    const int SZ = 10;
    char check[SZ] = { 1, 0 };
    for (T n = N; n > 0; n /= 10) check[n % 10] = 1;
    FOR(i, (int)SZ) if (!check[i]) return false;
    return true;
}


bool IsPandigital(const std::string& s, int begin, int end)
{
    const int SZ = 10;
    char check[SZ] = { 1, 0 };
    size_t N = s.size();
    if (end == -1) end = (int) (N - 1);
    if ((end - begin + 1) < 9 || s.size() < 9) return false;
    FORN(i, begin, end) check[s[i] - '0'] = 1;
    FOR(i, (int)SZ) if (!check[i]) return false;
    return true;
}


//template<> bool IsPandigital<char*>(const char*& s) {
bool IsPandigital(const char* s) {
    const int SZ = 10;
    char check[SZ] = { 1, 0 };
    int len = (int) strlen(s);
    FOR(i, len) check[s[i] - '0'] = 1;
    FOR(i, (int)SZ) if (!check[i]) return false;
    return true;
}


template<class T>
void UNQ(T& x)
{
    sort(ALL(x));
    x.resize(unique(ALL(x)) - x.begin());
}

//
// :::Numbers / :::Numeric
//

/**
 *  \brief Determines the sign of a given number
 *  
 *  \param [in] val Value
 *  
 *  \return -1 if val is -ve
 *           0 if val is zero
 *           1 if val is +ve
 */
template<typename T> int Sign(T val)
{
    return (T(0) < val) - (val < T(0));
}

//
// TODO: I think, it is better to create overloaded methods instead of template
// specialization...
//
int Sign(const char* szVal)
{
    if (!IsNumber(szVal)) {
        throw std::exception((std::string("\"") + szVal + "\" is not a number.").c_str());
    }
    return (szVal[0] == '-' ? -1 : 1);
}

int Sign(const std::string& val)
{
    if (!IsNumber(val)) {
        throw std::exception(("\"" + val + "\" is not a number.").c_str());
    }
    return (val[0] == '-' ? -1 : 1);
}


/**
 *  \brief Check if the given is a number
 *  
 *  \param [in] s String to check
 *  
 *  \return True if \a s is a number (int/float/double) otherwise false
 */
bool IsNumber(const std::string& s)
{
    std::regex re(R"([+-]{0,1}\d*[\.]{0,1}[\d]*)");
    return std::regex_match(s, re);
}


/**
 *  \brief  Return number of 1s in \a n in binary.
 *          
 *  \param[in]  n   Number
 *  
 *  \return     Return number of 1s in \a n in binary.
 *  
 *  \sa GetBinaryCardinality
 */
template<typename T>
int BitCount(T n)
{
    int ret = 0;
    while (n > 0) { ++ret; n = n & (n - 1); }
    return ret;
}


/**
 *  \brief  Return the minimum number of bits required to represent \a n
 *          as a binary number.
 *          
 *  \param[in]  n   Number
 *  
 *  \return     Minimum #bits required to represent \a n in a binary number.
 *  
 *  \sa BitCount
 */
template<typename T>
int BinaryCardinality(T n)
{
    return log2(n) + 1;
}


/**
 *  \brief  Returns the number of digits in a given \a N in its decimal
 *          representation.
 *          
 *  \param[in]  N   Number
 *  
 *  \return Number of digits in given number \a N
 *  
 *  \sa BitCount
 *  \sa BinaryCardinality
 */
template<typename T>
int DigitCount(T N)
{
    return N ? (int)(log10(1. * max(N, -N)) + 1) : 0;
}

/**
 *  \brief Checks if A is subset of B
 *  
 *  \param[in]  A   First number
 *  \param[in]  B   Second number
 *  
 *  \return True if A is subset of B, otherwise False.
 */
bool ASubsetOfB(unsigned int A, unsigned int B)
{
    return (A & B) == A;
}


/**
 *  \brief Factorial of a given number \a n
 *  
 *  \return Factorial of a given number \a n
 */
template<typename T> T Factorial(const T& n)
{
    return n == 0 ? 1 : n * Factorial(n - 1);
}


/**
 *  \brief NCR of given numbers \a n and \a r.
 *  
 *  \param[in]  n   N value
 *  \param[in]  r   R value
 *  
 *  \return NCR
 *  
 *  \code
 *  NCR(5, 0) = [1]
 *  NCR(5, 1) = [5]
 *  NCR(5, 2) = [10]
 *  NCR(5, 5) = [1]
 *  \endcode
 */
template<typename T>
T NCR(T n, T r)
{
    r = std::min<T>(r, n - r);
    T num = 1, den = Factorial<T>(r);
    for (; r > 0; --r) num *= n--;
    return (num / den);
}


/**
 *  \brief Checks if the given number \a n is bouncy.
 *  
 *  Working from left-to-right if no digit is exceeded by the digit to its left
 *  it is called an increasing number; for example, 134468.
 *
 *  Similarly if no digit is exceeded by the digit to its right it is called a
 *  decreasing number; for example, 66420.
 *
 *  We shall call a positive integer that is neither increasing nor decreasing
 *  a "bouncy" number; for example, 155349.
 *
 *  \param[in]  n   Number
 *  
 *  \return True if \a n is bouncy, otherwise False.
 *  
 *  \sa IsIncreasingNumber
 *  \sa IsStrictlyIncreasingNumber
 *  \sa IsDecreasingNumber
 *  \sa IsStrictlyDecreasingNumber
 *  
 *  \ref https://projecteuler.net/problem=112
 *  
 *  \code
 *  IsBouncy(155349) = [true]
 *  \endcode
 */
template<typename T>
bool IsBouncy(T n)
{
    bool increasing = false;
    bool decreasing = false;
    int prev = n % 10, cur;
    n /= 10;
    while (n > 0) {
        cur = n % 10;
        if (cur < prev) increasing = true;
        if (cur > prev) decreasing = true;
        if (increasing && decreasing) return true;
        prev = cur;
        n /= 10;
    }
    return false;
}


/**
 *  \brief Checks if the given number \a n is increasing or not.
 *  
 *  Working from left-to-right if no digit is exceeded by the digit to its left
 *  it is called an increasing number; for example, 134468.
 *  
 *  \param[in]  n   Number
 *  
 *  \return True if \a n is increasing, otherwise False.
 *  
 *  \sa IsStrictlyIncreasingNumber
 *  \sa IsDecreasingNumber
 *  \sa IsStrictlyDecreasingNumber
 *  \sa IsBouncy
 *  
 *  \ref https://projecteuler.net/problem=112
 *  
 *  \code
 *  IsIncreasingNumber(134468) = [true]
 *  IsIncreasingNumber(249)    = [true]
 *  IsIncreasingNumber(924)    = [false]
 *  \endcode
 */
template<typename T>
bool IsIncreasingNumber(T n)
{
    int right = n % 10, left;
    n /= 10;
    while (n > 0) {
        left = n % 10;
        if (left > right) return false;
        right = left;
        n /= 10;
    }
    return true;
}


template<typename T>
bool IsStrictlyIncreasingNumber(T n)
{
    int right = n % 10, left;
    n /= 10;
    while (n > 0) {
        left = n % 10;
        if (left >= right) return false;
        right = left;
        n /= 10;
    }
    return true;
}

/**
 *  \brief  Check if the given number \a n is decreasing or not.
 *  
 *  Working from left-to-right if no digit is exceeded by the digit to its
 *  right it is called a decreasing number; for example, 66420.
 *  
 *  \ref https://projecteuler.net/problem=112
 */
template<typename T>
bool IsDecreasingNumber(T n)
{
    int right = n % 10, left;
    n /= 10;
    while (n > 0) {
        left = n % 10;
        if (left < right) return false;
        right = left;
        n /= 10;
    }
    return true;
}

template<typename T>
bool IsStrictlyDecreasingNumber(T n)
{
    int right = n % 10, left;
    n /= 10;
    while (n > 0) {
        left = n % 10;
        if (left <= right) return false;
        right = left;
        n /= 10;
    }
    return true;
}

template<typename T> T NCR(int N, int R)
{
    R = std::min(R, N - R);
    std::vector<int> vi1, vi2;
    FORN(i, 1, R) vi1.push_back(N - i + 1);
    FORN(i, 1, R) vi2.push_back(i);

    while (true) {
        bool valid = false;
        FORC(i, vi1) {
            FORC(j, vi2) {
                int x = GCD(vi1[i], vi2[j]);
                if (x != 1) {
                    int v1 = vi1[i] / x;
                    int v2 = vi2[j] / x;
                    vi1.erase(vi1.begin() + i); vi1.push_back(v1);
                    vi2.erase(vi2.begin() + j); vi2.push_back(v2);
                    valid = true;
                    break;
                }
            }
        }
        if (!valid) break;
    }

    T ret = 1;
    FORC(i, vi1) ret *= vi1[i];
    FORC(i, vi2) ret /= vi2[i];
    return ret;
}

//
// For unsigned types -N (applying minus) is meaning less, so do not use
//  max(N, -N) for unsigned types.
//  
template<typename T> int GetNumberOfDigits(T N)
{
    //return N ? (int)(log10(1. * max(N, -N)) + 1) : 0;
    if (N == 0) return 0;
    if (N > 0)  return (int)(log10(1. * N) + 1);
    return (int)(log10(1. * -N) + 1);
}

// abs() doesn't work for long long that's why i have used max
template<typename T> T GCD(const T& a, const T& b)
{
    return a == 0 ? std::max<T>(b, -b) : GCD<T>(b % a, a);
}

template<> static UInt64 GCD(const UInt64& a, const UInt64& b)
{
    return a == 0 ? b : GCD<UInt64>(b % a, a);
}

template<typename T> T LCM(const T& a, const T& b)
{
    return a * b == 0 ? 0 : a * b / GCD<T>(a, b);
}


/**
 * \brief Compute the sum of digits in the given number.
 */
template<typename T> int GetDigitsSum(T N)
{
    return N > 0 ? N % 10 + GetDigitsSum(N / 10) : 0;
}


/**
 * \brief Compute the sum of digits in the given number string.
 */
int GetDigitsSum(const std::string& S) {
    int ret = 0;
    for (size_t i = 0; i < S.size(); ++i) ret += S[i] - '0';
    return ret;
}


/**
 *  \brief Convert the given number \a value (in decimal) to the requested base.
 *  
 *  \return String in base \a radix.
 *  
 *  \code
 *  ToRadix(N, 2)  = [11111001]
 *  ToRadix(N, 10) = [249]
 *  ToRadix(N, 16) = [F9]
 *  \endcode
 */
template<typename T>
std::string ToRadix(T value, int radix)
{
    std::string s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    std::string ret;
    while (value > 0) {
        int r = value % radix;
        ret = s[r] + ret;
        value /= radix;
    }
    return ret.empty() ? "0" : ret;
}

/*
 * This is the fastest method when compared to n == Reverse(n).
 * Please do NOT make any changes.
 */
template <typename T> bool IsPalindrome(T n)
{
    T divisor = 1;
    while (n / divisor >= 10) divisor *= 10;
    while (n != 0) {
        int leading = n / divisor;
        int trailing = n % 10;
        if (leading != trailing) return false;
        n = (n % divisor) / 10;
        divisor = divisor / 100;
    }
    return true;
}

template <typename T>
T GetCoinChanges(const std::vector<T>& vi, T n)
{
    // We need n + 1 rows as the table is constructed in bottom up 
    // manner using the base case 0 value case (n = 0)
    std::vector<std::vector<T>> dp(n + 1, std::vector<T>(vi.size()));

    int m = (int) vi.size();

    // Fill the entries for 0 value case (n = 0) 
    for (int i = 0; i < m; ++i) dp[0][i] = 1;

    // Fill rest of the table entries in bottom up manner  
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < m; ++j) {
            // Count of solutions including vi[j] 
            T x = (i - vi[j] >= 0) ? dp[i - vi[j]][j] : 0;

            // Count of solutions excluding vi[j]
            T y = (j >= 1) ? dp[i][j - 1] : 0;

            // total count 
            dp[i][j] = x + y;
        }
    }
    return dp[n][m - 1];
}

//
// :::~numeric
//

//
// :::Strings
//

template<typename T>
T ToLower(T s)
{
    for (size_t i = 0; i < s.size(); ++i)
        if (isupper(s[i]))
            s[i] += 32;
    return s;
}

template<typename T>
T ToUpper(T s)
{
    for (size_t i = 0; i < s.size(); ++i)
        if (islower(s[i]))
            s[i] -= 32;
    return s;
}

std::string ReplaceALL(std::string s, const std::string& fnd, const std::string& rep) {
    size_t pos = 0;
    while ((pos = s.find(fnd, pos)) != std::string::npos) {
        s.replace(pos, fnd.size(), rep);
        pos += rep.size();
    }
    return s;
}

std::string RemoveALL(const std::string& str, const std::string& seps)
{
    std::string ret;
    for (size_t p = 0, q; p != std::string::npos; p = q) {
        p = str.find_first_not_of(seps, p);
        if (p == std::string::npos) break;
        q = str.find_first_of(seps, p);
        ret.append(str.substr(p, q - p));
    }
    return ret;
}

/**
 * \brief   Gets current date time.
 *
 * \return  The current date time.
 */
std::string GetCurrentDateTimeA()
{
    char szDateTime[26] = { 0 };

    time_t startedClock;
    time(&startedClock);
    errno_t err;
    struct tm startedInfo;
    err = localtime_s(&startedInfo, &startedClock);

    if (!err) {
        err = asctime_s(szDateTime, _countof(szDateTime), &startedInfo);
        if (err) {
            sprintf_s(szDateTime, "%s %s", __TIME__, __DATE__);
        }
        else {
            szDateTime[24] = '\0';
        }
    }

    return szDateTime;
}

/**
 * \brief   Gets current date time.
 *
 * \return  The current date time.
 */
std::wstring GetCurrentDateTimeW()
{
    wchar_t szDateTime[26] = { 0 };

    time_t startedClock;
    time(&startedClock);
    errno_t err;
    struct tm startedInfo;
    err = localtime_s(&startedInfo, &startedClock);

    if (!err) {
        err = _wasctime_s(szDateTime, _countof(szDateTime), &startedInfo);
        if (err) {
            swprintf_s(szDateTime, L"%s %s", LGWSTR(__TIME__), LGWSTR(__DATE__));
        }
        else {
            szDateTime[24] = L'\0';
        }
    }

    return szDateTime;
}

#ifdef UNICODE
#define GetCurrentDateTime  GetCurrentDateTimeW
#else
#define GetCurrentDateTime  GetCurrentDateTimeA
#endif // !UNICODE


/**
 *  \brief Trim leading and trailing spaces (including tabs and newlines).
 *  
 *  \param[in, out]     s   C-style string.
 *  
 *  \return     String after removing leading and trailing spaces.
 */
char* Trim(char* s)
{
    if (s == NULL) return NULL;

    char* p = s + strlen(s) - 1;
    while (*p != '\0' && (*p == ' ' || *p == '\t' || *p == '\n')) --p; p[1] = '\0';
    while (*s != '\0' && (*s == ' ' || *s == '\t' || *s == '\n')) ++s;

    return s;
}


std::string Trim(const std::string& str, const std::string& seps)
{
    if (str.empty()) return str;
    size_t p = str.find_first_not_of(seps);
    if (p == std::string::npos) return "";
    size_t q = str.find_last_not_of(seps);
    return str.substr(p, q - p + 1);
}


std::string TrimLeft(const std::string& str, const std::string& seps)
{
    if (str.empty()) return str;
    size_t p = str.find_first_not_of(seps);
    if (p == std::string::npos) return "";
    size_t q = str.size();
    return str.substr(p, q - p + 1);
}


std::string TrimRight(const std::string& str, const std::string& seps)
{
    if (str.empty()) return str;
    size_t p = 0;
    size_t q = str.find_last_not_of(seps);
    return str.substr(p, q - p + 1);
}


bool IsPrefix(const std::string& s, const std::string& prefix)
{
    return s.find(prefix) == 0;
}


bool IsSuffix(const std::string& s, const std::string& suffix)
{
    return s.size() > suffix.size() &&
           s.rfind(suffix) == s.size() - suffix.size();
}


bool ASubsetOfB(const std::string& A, const std::string& B)
{
    for (size_t i = 0; i < A.size(); ++i)
        if (B.find(A[i]) == std::string::npos)
            return false;
    return true;
}

bool IsPalindrome(const std::string& s) {
    int N = (int) s.size();
    FOR(i, N >> 1) if (s[i] != s[N - i - 1]) return false;
    return true;
}

bool IsPalindrome(const std::string& s, int l, int r) {
    int N = (r - l + 1) / 2;
    FOR(i, N) if (s[l + i] != s[r - i]) return false;
    return true;
}

std::string LCSubString(const std::string& X, const std::string& Y) {
    int m = X.size();
    int n = Y.size();
    int len = 0;
    int end;
    int currRow = 0;
    std::vector<std::vector<int>> LCSuff(2, std::vector<int>(n + 1, 0));

    // The first row and first column entries have no logical meaning,  
    // they are used only for simplicity of program.
    // Following steps build LCSuff[m + 1][n + 1] in bottom up fashion. 
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (X[i - 1] == Y[j - 1]) {
                LCSuff[currRow][j] = LCSuff[1 - currRow][j - 1] + 1;
                len = std::max<int>(len, LCSuff[currRow][j]);
                end = i - 1;
            }
        }
        currRow = 1 - currRow;
    }
    return X.substr(end - len + 1, len);
}

// 
// :::~strings
// 

//
// :::Class / :::Struct
//

struct Sudoku {
    VVI m_In;
    VVI m_Out;
    std::vector<VVI> m_Results;

    Sudoku(const VVI& vvi) : m_In(vvi), m_Out(vvi) {}

    VVI Solve() {
        Solve(m_Out, 0);
        //LGPRINT(m_Res.size());
        return m_Results.empty() ? VVI() : m_Results[0];
    }

private:

    bool IsNotInBlk(VVI& vvi, int ele, int r, int c) {
        int row = r / 3, col = c / 3;
        for (int i = 3 * row; i < 3 * (row + 1); ++i)
            for (int j = 3 * col; j < 3 * (col + 1); ++j)
                if (ele == vvi[i][j]) return false;
        return true;
    }

    bool IsNotInRow(VVI& vvi, int ele, int row, int col) {
        FOR(i, 9) if (i != col && vvi[row][i] == ele) return false;
        return true;
    }

    bool IsNotInCol(VVI& vvi, int ele, int row, int col) {
        FOR(i, 9) if (i != row && vvi[i][col] == ele) return false;
        return true;
    }

    void Solve(VVI& res, int ct) {
        if (ct > 80) { m_Results.push_back(res); return; }
        int r = ct / 9, c = ct % 9;
        VVI tmp(res);

        if (m_In[r][c] != 0) Solve(res, ct + 1);

        FORN(digit, 1, 9) if (!m_In[r][c]) {
            if (!m_In[r][c] &&
                IsNotInBlk(res, digit, r, c) &&
                IsNotInRow(res, digit, r, c) &&
                IsNotInCol(res, digit, r, c))
            {
                res[r][c] = digit;
                if (ct == 80) {
                    m_Results.push_back(res);
                }
                else{
                    Solve(res, ct + 1);
                    res = tmp;
                }
            }
        }
    }
};


/**
 * StreamReader
 */
struct StreamReader
{
    std::string     m_FilePath;
    std::fstream    m_fs;

    StreamReader(const std::string& path) : m_FilePath(path), m_fs(path) {
        if (!m_fs.is_open()) {
            throw std::exception(std::string("Filed not open input file [" + path + "].").c_str());
        }
    }

    ~StreamReader() { Close(); }

    void Close() {
        if (m_fs.is_open()) {
            m_fs.close();
        }
    }

    std::string ReadLine() {
        std::string line;
        std::getline(m_fs, line);
        return line;
    }

    bool ReadLine(std::string& line) {
        if (m_fs.eof()) return false;
        std::getline(m_fs, line);
        return true;
    }

    template<typename T> bool Read(T& t) {
        return (bool)(m_fs >> t);
    }

    template<typename T> bool Read(std::vector<std::vector<T>>& t) {
        t.clear();
        std::vector<T> vt;
        while (m_fs >> vt) {
            if (vt.empty()) return true;
            t.push_back(vt);
        }
        return true;
    }

    template<class T> T ToVal(const std::string& s) { T ret; std::istringstream iss(s); iss >> ret; return ret; }

    std::string Trim(const std::string& str, std::string seps = " ")
    {
        if (str.empty()) return str;
        size_t p = str.find_first_not_of(seps);
        if (p == std::string::npos) return "";
        size_t q = str.find_last_not_of(seps);
        return str.substr(p, q - p + 1);
    }

    template <typename T> bool Read(std::vector<T>& vt, const std::string& seps) {
        vt.clear();
        std::string line;
        ReadLine(line);
        line = Trim(line);
        for (size_t p = 0, q = 0; q != std::string::npos; p = q) {
            p = line.find_first_not_of(seps, p);
            if (p == std::string::npos) break;
            q = line.find_first_of(seps, p);
            vt.push_back(ToVal<T>(line.substr(p, q - p)));
        }
        return true;
    }

    template<typename T> bool Read(std::vector<std::vector<T>>& vvt, const std::string& seps) {
        vvt.clear();
        std::vector<T> vt;
        while (Read(vt, seps)) {
            if (vt.empty()) return true;
            vvt.push_back(vt);
        }
        return true;
    }

    template<typename T> T Read() {
        T t;
        if (!(m_fs >> t)) {
            std::string typeName = GetTypeName(t);
            throw std::exception(std::string("failed to read <" + typeName + ">.").c_str());
        }
        return t;
    }

    bool IsEOF() { return m_fs.eof(); }

    operator bool() { return !m_fs.eof(); }
};


/**
 *  \brief Roman Converter
 *  
 *  I = 1
 *  V = 5
 *  X = 10
 *  L = 50
 *  C = 100
 *  D = 500
 *  M = 1000
 *
 *  Rules:
 * 
 *  (1) Only I, X, and C can be used as the leading numeral in part of a subtractive pair.
 *  (2) I can only be placed before V and X.
 *  (3) X can only be placed before L and C.
 *  (4) C can only be placed before D and M.
 */
struct Roman
{
    static long Get(const char ch) {
        switch (toupper(ch)) {
        case 'I': return    1;
        case 'V': return    5;
        case 'X': return   10;
        case 'L': return   50;
        case 'C': return  100;
        case 'D': return  500;
        case 'M': return 1000;
        }
        return 0;
    }

    static long Convert(const std::string& romanNumeral) {
        long ret = 0;
        char prev = '\0';
#if __LGCPP11   /* VisualStudio 2012, VC++ compiler */
        FOREACH(_ch, romanNumeral) {
#else
        FOREACH(std::string, it, romanNumeral) {
            decltype(*it) ch = *it;
#endif
            char ch = toupper(_ch);
            ret += Get(ch);
            if (prev && Get(prev) < Get(ch)) {
                ret -= (Get(prev) << 1);
            }
            prev = (ch == 'I' || ch == 'X' || ch == 'C') ? ch : '\0';
        }
        return ret;
    }

    static std::string Convert(long decimal)
    {
        const int   N = 13;
        long        dec[N] = { 1000, 900,  500, 400,  100,  90,  50,  40,   10,   9,    5,   4,    1  };
        std::string num[N] = {  "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };
        std::string numeral;

        FOR(i, (int)N) {
            while (decimal >= dec[i]) {
                decimal -= dec[i];
                numeral.append(num[i]);
            }
        }

        return numeral;
    }
};


template<typename T>
struct Triangle2D
{
    Point2D<T> A, B, C;

    Triangle2D(const Point2D<T>& a, const Point2D<T>& b, const Point2D<T>& c) : A(a), B(b), C(c) {}

    bool IsRight() {
        T ab = (A.X - B.X) * (A.X - B.X) + (A.Y - B.Y) * (A.Y - B.Y);
        T bc = (B.X - C.X) * (B.X - C.X) + (B.Y - C.Y) * (B.Y - C.Y);
        T ca = (A.X - C.X) * (A.X - C.X) + (A.Y - C.Y) * (A.Y - C.Y);
        return (ab == bc + ca || bc == ab + ca || ca == ab + bc);
    }
};


/**
 *  \brief StopWatch
 */
struct StopWatch
{
    void Start() {
        QueryPerformanceCounter(&m_tStartTime);
    }

    double Stop() {
        QueryPerformanceCounter(&m_tStopTime);
        QueryPerformanceFrequency(&m_tFrequency);

        return (double)(m_tStopTime.QuadPart - m_tStartTime.QuadPart) / (double)m_tFrequency.QuadPart;
    }

private:
    LARGE_INTEGER m_tStartTime;
    LARGE_INTEGER m_tStopTime;
    LARGE_INTEGER m_tFrequency;
};


/**
 *  \brief ScoppedTimer
 */
struct ScopedTimer
{
    ScopedTimer(const std::string name = std::string(""))
        : m_Name(name)
    {
        QueryPerformanceCounter(&m_tStartTime);
        m_Started = GetCurrentDateTimeA();
        if (!m_Name.empty()) {
            printf_s("[%s] Started : %s\n", m_Name.c_str(), m_Started.c_str());
        } else {
            printf_s("Started : %s\n", m_Started.c_str());
        }
    }

    ~ScopedTimer() {
        QueryPerformanceCounter(&m_tStopTime);
        QueryPerformanceFrequency(&m_tFrequency);
        m_Elapsed = (double)(m_tStopTime.QuadPart - m_tStartTime.QuadPart) / (double)m_tFrequency.QuadPart;

        m_Ended = GetCurrentDateTimeA();
        if (!m_Name.empty()) {
            printf_s("[%s] Ended   : %s\n", m_Name.c_str(), m_Ended.c_str());
            printf_s("[%s] Elapsed : %f\n", m_Name.c_str(), m_Elapsed);
        } else {
            printf_s("Ended   : %s\n", m_Ended.c_str());
            printf_s("Elapsed : %f\n", m_Elapsed);
        }
    }

private:

    LARGE_INTEGER   m_tStartTime;
    LARGE_INTEGER   m_tStopTime;
    LARGE_INTEGER   m_tFrequency;
    std::string     m_Started;
    std::string     m_Ended;
    double          m_Elapsed;
    std::string     m_Name;
};

//
// :::~class / :::~struct
// 

//
// :::Algorithms
//
// Kruskal's Minimum Spanning Tree
std::vector<std::pair<int, int>> SpanningTree_Kruskals(std::vector<std::vector<int>> a)
{
    struct Node {
        int i, j, cost;
        Node() {}
        Node(int _i, int _j, int _cost) : i(_i), j(_j), cost(_cost) { }
        bool operator < (const Node& rhs) const { return cost > rhs.cost; }
    };

    std::priority_queue<Node> q;
    int n = (int)a.size(), cc = 0;
    FOR(i, n) FOR(j, n) if (i < j && a[i][j] != -1) q.push(Node(i, j, a[i][j]));
    std::vector<std::set<int>> sts(n);
    FOR(i, n) sts[i].insert(i);
    std::vector<std::pair<int, int>> ret;

    while (!q.empty()) {
        Node no = q.top(); q.pop();
        int i = no.i; int j = no.j;
        int s1, s2;
        for (int k = 0; k < (int)sts.size(); ++k) {
            if (sts[k].count(i)) s1 = k;
            if (sts[k].count(j)) s2 = k;
        }
        if (s1 == s2) continue;
        cc++;
        sts[s1].insert(ALL(sts[s2])); sts[s2].clear();
        ret.push_back(std::make_pair(i, j));
        if (cc == n - 1) break;
    }
    if (cc != n - 1) { ret.clear(); }
    return ret;
}

// Prims Minimum Spanning Tree
std::vector<std::pair<int, int>> SpanningTree_Prims(std::vector<std::vector<int>> a)
{
    int N = (int)a.size();
    std::vector<std::pair<int, int>> ret, edges;
    FOR(i, N) FOR(j, N) if (i < j && a[i][j] != -1) edges.push_back(std::make_pair(i, j));
    std::set<int> vertices, verticesNew;
    FOR(i, N) vertices.insert(i);
    verticesNew.insert(0);

    while (verticesNew != vertices) {
        std::pair<int, int> newedge;
        int cost = INT_MAX;
        FORC(i, edges) {
            int u = edges[i].first, v = edges[i].second, c = a[u][v];
            if (find(ALL(verticesNew), u) == verticesNew.end() || find(ALL(verticesNew), v) != verticesNew.end()) {
                std::swap(u, v);
                if (find(ALL(verticesNew), u) == verticesNew.end() || find(ALL(verticesNew), v) != verticesNew.end())
                    continue;
            }
            if (cost > c) {
                newedge.first = u;
                newedge.second = v;
                cost = a[u][v];
            }
        }
        ret.push_back(newedge);
        verticesNew.insert(newedge.second);
        std::vector< std::pair<int, int> >::iterator it = find(ALL(edges), newedge);
        if (it == edges.end()) {
            std::swap(newedge.first, newedge.second);
            it = find(ALL(edges), newedge);
        }
        edges.erase(it);
    }

    return ret;
}


//
// Simple expression evaluator
// Ref: http://www.strchr.com/expression_evaluator
// (c) Peter Kankowski, 2007.
// http://smallcode.weblogs.us mailto:kankowski@narod.ru
// 
class ExprEval {
    // Error codes
    enum EXPR_EVAL_ERR {
        EEE_NO_ERROR        = 0,
        EEE_PARENTHESIS     = 1,
        EEE_WRONG_CHAR      = 2,
        EEE_DIVIDE_BY_ZERO  = 3
    };

    typedef char EVAL_CHAR;

private:

    EXPR_EVAL_ERR   _err;
    EVAL_CHAR*      _err_pos;
    int             _paren_count;

    // Parse a number or an expression in parenthesis
    double ParseAtom(EVAL_CHAR*& expr) {
        // Skip spaces
        while (*expr == ' ')
            expr++;

        // Handle the sign before parenthesis (or before number)
        bool negative = false;
        if (*expr == '-') {
            negative = true;
            expr++;
        }
        if (*expr == '+') {
            expr++;
        }

        // Check if there is parenthesis
        if (*expr == '(') {
            expr++;
            _paren_count++;
            double res = ParseSummands(expr);
            if (*expr != ')') {
                // Unmatched opening parenthesis
                _err = EEE_PARENTHESIS;
                _err_pos = expr;
                return 0;
            }
            expr++;
            _paren_count--;
            return negative ? -res : res;
        }

        // It should be a number; convert it to double
        char* end_ptr;
        double res = strtod(expr, &end_ptr);
        if (end_ptr == expr) {
            // Report error
            _err = EEE_WRONG_CHAR;
            _err_pos = expr;
            return 0;
        }
        // Advance the pointer and return the result
        expr = end_ptr;
        return negative ? -res : res;
    }

    // Parse multiplication and division
    double ParseFactors(EVAL_CHAR*& expr) {
        double num1 = ParseAtom(expr);
        for (;;) {
            // Skip spaces
            while (*expr == ' ')
                expr++;
            // Save the operation and position
            EVAL_CHAR op = *expr;
            EVAL_CHAR* pos = expr;
            if (op != '/' && op != '*')
                return num1;
            expr++;
            double num2 = ParseAtom(expr);
            // Perform the saved operation
            if (op == '/') {
                // Handle division by zero
                if (num2 == 0) {
                    _err = EEE_DIVIDE_BY_ZERO;
                    _err_pos = pos;
                    return 0;
                }
                num1 /= num2;
            }
            else
                num1 *= num2;
        }
    }

    // Parse addition and subtraction
    double ParseSummands(EVAL_CHAR*& expr) {
        double num1 = ParseFactors(expr);
        for (;;) {
            // Skip spaces
            while (*expr == ' ')
                expr++;
            EVAL_CHAR op = *expr;
            if (op != '-' && op != '+')
                return num1;
            expr++;
            double num2 = ParseFactors(expr);
            if (op == '-')
                num1 -= num2;
            else
                num1 += num2;
        }
    }

public:

    double Eval(EVAL_CHAR* expr) {
        _paren_count = 0;
        _err = EEE_NO_ERROR;
        double res = ParseSummands(expr);
        // Now, expr should point to '\0', and _paren_count should be zero
        if (_paren_count != 0 || *expr == ')') {
            _err = EEE_PARENTHESIS;
            _err_pos = expr;
            return 0;
        }
        if (*expr != '\0') {
            _err = EEE_WRONG_CHAR;
            _err_pos = expr;
            return 0;
        }
        return res;
    };

    EXPR_EVAL_ERR GetErr() { return _err; }
    EVAL_CHAR* GetErrPos() { return _err_pos; }
};


/**
 * \brief PrintFormatter or FormatPrinter
 * 
 * You can use this class to print as shown below:
 *
 *           Name : Lokesh Govindu
 *        Company : Hexagon Geospatial
 *    Designation : Software Developer
 *
 * Constructor take two arguments width and sep:
 * 
 * (1) Width     : Left side part width, default 15 characters, you can also
 *                 Specify width in negative, which aligns the text to left.
 *                 Default +15 (right justification)
 *                 
 * (2) Separator : Character to be placed between key & value.
 *                 Default is ':' (colon)
 */
struct PrintFormatter
{
    int     m_Width;
    _TCHAR  m_Sep;
    _TCHAR  m_Fmt[256];

    PrintFormatter(int width = 15, _TCHAR sep = _TCHAR(':'))
        : m_Width(width)
        , m_Sep(sep)
    {
        _stprintf_s(m_Fmt, _T("%%%ds %c "), m_Width, m_Sep);
        //_tprintf_s(_T("Fmt = [%s]\n"), m_Fmt);
    }

    void Write(const _TCHAR* key, const _TCHAR* fmt, ...)
    {
        _tprintf_s(m_Fmt, key);

        va_list tArgs;
        va_start(tArgs, fmt);
        _vtprintf_s(fmt, tArgs);

        _tprintf_s(_T("\r\n"));
    }

    void Write(const _TCHAR* fmt, ...)
    {
        va_list tArgs;
        va_start(tArgs, fmt);
        _vtprintf_s(fmt, tArgs);

        _tprintf_s(_T("\r\n"));
    }
};

class DijkstraAlgorithm {
    struct Node {
        int r;
        int c;
        int cost;
        Node(int _r, int _c, int _cost) : r(_r), c(_c), cost(_cost) {}
        bool operator < (const Node& other) const {
            return cost > other.cost;
        }
    };

    std::vector<std::vector<int>> vvi;
    int R;
    int C;
    int sourceRow;
    int sourceCol;
    int targetRow;
    int targetCol;
    std::vector<short> vdr;
    std::vector<short> vdc;

    int minCost;

public:
    explicit DijkstraAlgorithm(const std::vector<std::vector<int>>& _vvi,
        int sourceRow, int sourceCol,
        int targetRow, int targetCol,
        int numDirections = 4)
        : vvi(_vvi)
    {
        this->R = (int) vvi.size();
        this->C = (int) vvi[0].size();

        this->sourceRow = sourceRow;
        this->sourceCol = sourceCol;
        this->targetRow = targetRow;
        this->targetCol = targetCol;

        if (numDirections == 4) {
            vdr = { 0, 1,  0, -1 };
            vdc = { 1, 0, -1,  0 };
        }
        else {
            vdr = { -1, 0, 1, 1,  1,  0, -1, -1 };
            vdc = {  1, 1, 1, 0, -1, -1, -1,  0 };
        }

        // Returns
        minCost = -1;
    }

    int getMinimumCost() {
        std::vector<std::vector<bool>> visited(R, std::vector<bool>(C, false));
        std::priority_queue<Node> pq;
        Node node(sourceRow, sourceCol, vvi[sourceRow][sourceCol]);
        pq.push(node);
        while (!pq.empty()) {
            node = pq.top(); pq.pop();
            
            if (node.r == targetRow && node.c == targetCol) {
                minCost = node.cost;
                return minCost;
            }

            if (visited[node.r][node.c]) continue;
            visited[node.r][node.c] = true;

            FOR(i, vdr.size()) {
                int r = node.r + vdr[i];
                int c = node.c + vdc[i];
                if (r >= 0 && r < R && c >= 0 && c < C && !visited[r][c]) {
                    pq.push(Node(r, c, node.cost + vvi[r][c]));
                }
            }
        }
        return -1;
    }
};

template<typename T>
struct SubsetSum {
    std::vector<T> vi;
    bool printTable;

    SubsetSum(const T* A, int N) {
        this->printTable = false;
        FOR(i, N) this->vi.push_back(A[i]);
    }

    SubsetSum(const std::vector<T>& _vi) : vi(_vi), printTable(false) {}

    bool Solve(T sum) {
        T viSum = std::accumulate(ALL(vi), 0);
        if (viSum < sum) return false;
        if (viSum == sum) return true;

        int n = (int) vi.size();

        // The value of subset[i][j] will be true if there is a subset of
        // set[0..j-1] with sum equal to i
        std::vector<std::vector<bool>> subset(sum + 1, std::vector<bool>(n + 1, false));

        // If sum is 0, then answer is true
        FORN(i, 0, n) subset[0][i] = true;

        // If sum is not 0 and set is empty, then answer is false
        FORN(i, 1, sum) subset[i][0] = false;

        // Fill the subset table in bottom up manner
        FORN(i, 1, sum) {
            FORN(j, 1, n) {
                subset[i][j] = subset[i][j - 1] ||
                               (i >= vi[j - 1] ? subset[i - vi[j - 1]][j - 1] : subset[i][j - 1]);
            }
        }

        // Change if condition to true to print table.
        if (this->printTable) {
            printf_s("     |     ");
            FOR(j, n) printf_s("%4d", vi[j]);
            printf_s("\n");
            printf_s(" Sum | ");
            FORN(j, 0, n) printf_s("%4d", j);
            printf_s("\n");
            printf_s("----------------------------------------------------------------------\n");
            FORN(i, 0, sum) {
                printf_s("%4d | ", i);
                FORN(j, 0, n) {
                    printf_s("%4d", subset[i][j] ? 1 : 0);
                }
                printf_s("\n");
            }
        }

        return subset[sum][n];
    }

    std::vector<T> Backtrack(T sum) {
        T viSum = std::accumulate(ALL(vi), 0);
        if (viSum < sum) return std::vector<T>();
        if (viSum == sum) {
            std::vector<T> ret(vi.size());
            std::iota(ALL(ret), 0);
            return ret;
        }

        int n = (int)vi.size();

        // The value of subset[i][j] will be true if there is a subset of
        // set[0..j-1] with sum equal to i
        std::vector<std::vector<bool>> subset(sum + 1, std::vector<bool>(n + 1, false));

        // If sum is 0, then answer is true
        FORN(i, 0, n) subset[0][i] = true;

        // If sum is not 0 and set is empty, then answer is false
        FORN(i, 1, sum) subset[i][0] = false;

        // Fill the subset table in bottom up manner
        FORN(i, 1, sum) {
            FORN(j, 1, n) {
                subset[i][j] = subset[i][j - 1] ||
                    (i >= vi[j - 1] ? subset[i - vi[j - 1]][j - 1] : subset[i][j - 1]);
            }
        }

        if (!subset[sum][n]) return vector<T>();

        std::vector<T> ret;
        for (int s = sum, ind = n; s != 0;) {
            while (ind > 0 && subset[s][ind - 1]) --ind;
            ret.push_back(ind - 1);
            s -= this->vi[ind - 1];
        }
        std::reverse(ALL(ret));
        return ret;
    }
};

LOGO_NS_END /* LoGo namespace ends here! */

#endif /* __cplusplus ends here! */

#endif /* __LoGo_H__ */
