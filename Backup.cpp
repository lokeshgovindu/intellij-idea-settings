/*
  ___________________________
  \                         /
   \                       /
    \_____________________/
    |                     |
    |   T o p C o d e r   |
    |                     |
    /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\
   /                       \
  /                         \
  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
*/

    \_____________________/
    |                     |
    |   T o p C o d e r   |
    |                     |
    /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\

/*
//======================================================================================================================
::Endianness
    the order in which bytes in a multibyte word are stored. In a big endian machine
	the most significant byte of the word is stored at the lowest address of the word;
	in a little endian machine, the most significant byte is stored at the highest address.
	Big endian machines include SPARC and PowerPC. Little endian processors include the Intel x86.

    The table below shows the effects of endianness where:

    unsigned int value = 0x01020304;
    unsigned char* p = (unsigned char*)&value;
 
	----------+---------------------+-------------------
    | Address | Little Endian Value | Big Endian Value |
	----------+---------------------+-------------------
    | *p      |         0x04        |     0x01         |                 
    | *(p+1)  |         0x03        |     0x02         |              
    | *(p+2)  |         0x02        |     0x03         |              
    | *(p+3)  |         0x01        |     0x04         |
	----------+---------------------+-------------------
	
    Figure 5:  Endianness and Byte Order
//======================================================================================================================

*/

// http://channel9.msdn.com/Events/GoingNative/GoingNative-2012/Keynote-Bjarne-Stroustrup-Cpp11-Style
//______________________________________________________________________________________________________________________

//
//
//      +---------------------------------------------+
//      |                                             |
//      |   L o k e s h  G o v i n d u's C++ Backup   |
//      |                                             |
//      +---------------------------------------------+
//
//

//______________________________________________________________________________________________________________________

//     TopCoder : http://www.topcoder.com/tc?module=MemberProfile&cr=22650492
//   Codeforces : http://codeforces.com/profile/lokeshgovindu
// Projecteuler : http://projecteuler.net/profile/lokeshgovindu.png

// http://mathalon.in/

//______________________________________________________________________________________________________________________

/*

The more you understand, the less you have to memorize.   - HeadFirst Python
Palanadi naa sontam anukunnappatnunche neelo bayam modalavutundi. - Raveendranath Tagore
The future depends on what we do in the present. - Mahatma Gandhi

*/

//______________________________________________________________________________________________________________________

#pragma warning(disable:4786)
#pragma warning(disable:4244) // conversion double - int
#pragma warning(disable:4267) // conversion size_t - int
#pragma warning(disable:4018) // signed/unsigned comparision

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory>

using namespace std;
 
//______________________________________________________________________________________________________________________

typedef vector< int >               VI;
typedef vector< string >            VS;
typedef vector< double >            VD;
typedef vector< vector< double > >  VVD;
typedef vector< vector< string > >  VVS;
typedef vector< vector< int > >     VVI;

/* Built-in datatypes in C/C++ */
typedef signed char        Int8;
typedef signed short       Int16;
typedef signed int         Int32;
typedef signed long long   Int64;
typedef signed __int64     Int64;
typedef unsigned char      UInt8;
typedef unsigned short     UInt16;
typedef unsigned int       UInt32;
typedef unsigned long long UInt64;
typedef unsigned __int64   UInt64;
typedef char               Char;
typedef float              Float;
typedef float              Single;
typedef double             Double;

#if defined(__cplusplus)
typedef bool               Boolean;
typedef string             String;
#else
typedef unsigned char      Boolean;
#define MAX_STRING_LEN     256
typedef char               String[MAX_STRING_LEN];
#endif

//______________________________________________________________________________________________________________________

#define MPI 3.14159265358979323846264338327950288419716939937510

//______________________________________________________________________________________________________________________
#define MAX(x, y)                    ((x) > (y) ? (x) : (y))
#define MIN(x, y)                    ((x) < (y) ? (x) : (y))

#define CHR(x)                      #@x
#define STR_(x)                     #x
#define STR(x)                      STR_(x)
#define SIZE(C)                     C.size() 
#define ALL(C)                      (C).begin(), (C).end() 

#define ARRAY_SIZE(A)               (sizeof(A) / sizeof(A[0]))
#define ARRAY_ALL(A)                (A), (A) + ARRAY_SIZE(A)

#define MAKE_VECTOR(V, T, A)        std::vector<T> V = std::vector<T>(A, A + (sizeof(A) / sizeof(A[0])))

#define FOR(i, N)                   for (long i = 0; i < (N); ++i)
#define FORC(i, C)                  for (long i = 0; i < (C).size(); ++i)
#define FORN(i, x, n)               for (long i = x; i <= (n); ++i)

#if _MSC_VER >= 1700	/* VisualStudio 2012, VC++ compiler */
#define FOREACH(x, C)               for (auto& x : C)
#else
#define FOREACH(T, it, C)           for (T::iterator it = (C).begin(); it != (C).end(); ++it)
#endif

#define DEG_TO_RAD(deg)             ((deg * 2.0 * MPI) / 360.0)
#define RAD_TO_DEG(rad)             ((360.0 / (2.0 * MPI)) * rad)

#define TIME(t)                     clock_t t = clock()
#define TIME_DIFF(t1, t2)           (1.0 * abs(t2 - t1) / CLOCKS_PER_SEC)
#define	PRINT_TIME(exp)	{														\
	TIME(t1);																	\
	exp;																		\
	TIME(t2);																	\
	std::string str = STR(exp);													\
	if (str.size() > 40) { str.resize(36); str += " ..."; }						\
	str += " [Line: #" STR(__LINE__) "]";										\
	std::cout <<	str <<	" : " << TIME_DIFF(t1, t2) << " s" << std::endl;	\
}

#define REDIRECTSTDOUT(filepath)                                        \
    printf_s("Redirecting stdout to [%s]. @ Func : %s, Line : %d\n",    \
        filepath, __FUNCTION__, __LINE__);                              \
    freopen_s((FILE**)stdout, filepath, "w+t", stdout)                  \
	
#define FIND(C, V)                  (find(C.begin(), C.end(), V) != C.end())

#define INDEXOF(ind, C, V)										\
	auto ind = -1;												\
	{															\
		auto it = std::find(C.begin(), C.end(), V);				\
		ind = (it != indexes.end() ? it - C.begin() : -1);		\
	}

template<typename T>
inline int IndexOf(const vector<T>& C, const T& V) {
	std::vector<T>::const_iterator it = std::find(C.begin(), C.end(), V);
	return (it == C.end() ? -1 : (it - C.begin()));
}

#define TRACE(x)                    cerr << (x) << endl
#define CRLF                        cout << endl
#define PRINT(x)                    std::cout << STR(x) << " = [" << (x) << "]" << std::endl
#define PRINT2(a, b)						\
	std::cout								\
		<< STR(a) << " = " << (a)			\
		<< ", " << STR(b) << " = " << (b)	\
		<< std::endl

#define PRINT3(a, b, c)						\
	cout									\
		<< STR(a) << " = " << (a)			\
		<< ", " << STR(b) << " = " << (b)	\
		<< ", " << STR(c) << " = " << (c)	\
		<< std::endl

#define PRINT4(a, b, c, d)					\
	cout									\
		<< STR(a) << " = " << (a)			\
		<< ", " << STR(b) << " = " << (b)	\
		<< ", " << STR(c) << " = " << (c)	\
		<< ", " << STR(d) << " = " << (d)	\
		<< std::endl

#define LGPRINT_ARRAY(A) {                                      \
    int LGCAT(A, _Len) = sizeof(A) / sizeof(A[0]);              \
    printf_s("%s[%d] = [", LGSTR(A), LGCAT(A, _Len));           \
    printf_s("%d", A[0]);                                       \
    FORN(LGCAT(A, _ind), 1, LGCAT(A, _Len) - 1) {               \
        printf_s(", %d", A[LGCAT(A, _ind)]);                    \
    }                                                           \
    printf_s("]\n");                                            \
}

#define LGPRINT_ARRAYN(A, N) {                                  \
    printf_s("%s[%d] = [", LGSTR(A), N);                        \
    printf_s("%d", A[0]);                                       \
    FORN(LGCAT(A, _ind), 1, N - 1) {                            \
        printf_s(", %d", A[LGCAT(A, _ind)]);                    \
    }                                                           \
    printf_s("]\n");                                            \
}

//______________________________________________________________________________________________________________________

#define FILE_OPEN(fs, path)                                             \
    fstream fs(path);                                                   \
    if (fs.is_open() == false) {                                        \
        cout << "file not opened" << endl;                              \
        exit(-1);                                                       \
    }                                                                   \
//______________________________________________________________________________________________________________________

#define	PRINT_TIME(exp)	{													\
	TIME(t1);																\
	exp;																	\
	TIME(t2);																\
	std::string str = STR(exp);												\
	cout <<	str <<	" : " << TIME_DIFF(t1, t2) << " s" << endl;				\
}																			\
    
//______________________________________________________________________________________________________________________

// 2D DP
int dr[] = { 0,  1,  0, -1 };
int dc[] = { 1,  0, -1,  0 };

// 2D DP
int dr[] = { -1,  0,  1,  1,  1,  0, -1, -1 };
int dc[] = {  1,  1,  1,  0, -1, -1, -1,  0 };

//______________________________________________________________________________________________________________________

#define max(a,b) (((a) > (b)) ? (a) : (b))
#define min(a,b) (((a) < (b)) ? (a) : (b))
#define maxvi(vi) (*max_element (ALL(vi)))
#define minvi(vi) (*min_element (ALL(vi)))

//______________________________________________________________________________________________________________________
// String Convert
template<class T> std::string ToString(T x) { std::stringstream ss; ss << x; return ss.str(); }
template<class T> T ToVal(const string& s) { T ret; istringstream iss(s); iss >> ret; return ret; }

template<class T> string ToBinary(T N) {
    string ret;
    while(N > 0) {
        ret = (N & 1 ? '1' : '0') + ret;
        N = N >> 1;
    }
    return ret;
}

//______________________________________________________________________________________________________________________

#define MPI 3.14159265358979323846264338327950288419716939937510

//______________________________________________________________________________________________________________________

#define max(a, b) (((a) > (b)) ? (a) : (b))
#define min(a, b) (((a) < (b)) ? (a) : (b))
#define maxvi(vi) (*max_element(ALL(vi)))
#define minvi(vi) (*min_element(ALL(vi)))

//______________________________________________________________________________________________________________________

string toLower(string s) { for(int i = 0; i < s.size(); ++i) if(isupper(s[i])) s[i] += 32; return s; }
string toUpper(string s) { for(int i = 0; i < s.size(); ++i) if(islower(s[i])) s[i] -= 32; return s; }

//______________________________________________________________________________________________________________________

char* Trim(char* s) {
    char* p = NULL;
    if (s == NULL) return NULL;
    p = s + strlen(s) - 1;

    while(*p != '\0' && *p == ' ') --p; p[1] = '\0';
    while(*s != '\0' && *s == ' ') ++s;

    return s;
}

string Trim(const string& str, string seps = " ")
{
	if (str.empty()) return str;
	size_t p = str.find_first_not_of(seps);
	if (p == string::npos) return "";
	size_t q = str.find_last_not_of(seps);
	return str.substr(p, q - p + 1);
}

string TrimLeft(const string& str, string seps = " ")
{
    if (str.empty()) return str;
    size_t p = str.find_first_not_of (seps);
	if (p == string::npos) return "";
    size_t q = str.size();
    return str.substr (p, q - p + 1);
}

string TrimRight(const string& str, string seps = " ")
{
    if (str.empty()) return str;
    size_t p = 0;
    size_t q = str.find_last_not_of (seps);
    return str.substr (p, q - p + 1);
}

//______________________________________________________________________________________________________________________

string ReplaceALL(string s, string fnd, string rep = "") {
    size_t pos = 0;
    while ((pos = s.find(fnd, pos)) != string::npos) {
        s.replace(pos, fnd.size(), rep);
        pos += rep.size();
    }
    return s;
}

std::string RemoveALL(const std::string& str, const std::string& seps)
{
	std::string ret;
	for (size_t p = 0, q; p != string::npos; p = q) {
		p = str.find_first_not_of(seps, p);
		if (p == string::npos) break;
		q = str.find_first_of(seps, p);
		ret.append(str.substr(p, q - p));
	}
	return ret;
}

//______________________________________________________________________________________________________________________

template<typename T> ostream& operator << (ostream& out, const vector<T>& V) {
	if (V.empty()) return out;
	out << "{ " << V[0];
	for (int i = 1; i < (int)V.size(); ++i) out << ", " << V[i];
	out << " }";
	return out;
}

template <typename T> stringstream& operator >> (stringstream& ss, std::vector<T>& v) {
	v.clear();
	T val;
	while (ss >> val) { v.push_back(val); }
	return ss;
}

template <typename T> fstream& operator >> (fstream& fs, std::vector<T>& v) {
	v.clear();
	std::string line;
	std::getline(fs, line);
	// just return if line is empty.
	size_t p = line.find_first_not_of(" ", 0);
	if (p == std::string::npos) return fs;
	size_t q = line.find_last_not_of(" ");
	line = line.substr(p, q - p + 1);
	stringstream ss(line);
	T val;
	while (ss >> val) { v.push_back(val); }
	return fs;
}

//______________________________________________________________________________________________________________________

template <typename T>
std::vector<T> Split(const std::string& s, const string& seps = " ") {
	std::vector<T> ret; T val;
	for (size_t p = 0, q; p != string::npos; p = q) {
		p = s.find_first_not_of(seps, p);
		if (p == string::npos) break;
		q = s.find_first_of(seps, p);
		std::istringstream iss(s.substr(p, q - p));
		iss >> val;
		ret.push_back(val);
	}
	return ret;
}

std::vector<std::string> Split(const std::string& s, const std::string& seps = " ") {
	std::vector<std::string> ret;
	for (size_t p = 0, q; p != string::npos; p = q) {
		p = s.find_first_not_of(seps, p);
		if (p == string::npos) break;
		q = s.find_first_of(seps, p);
		ret.push_back(s.substr(p, q - p));
	}
	return ret;
}

//______________________________________________________________________________________________________________________

bool IsPrefix(const string& s, const string& sPrefix) { return s.find(sPrefix) == 0; }

bool IsSuffix(const string& s, const string& sSuffix) { return s.size() > sSuffix.size() && s.rfind(sSuffix) == s.size() - sSuffix.size(); }

//______________________________________________________________________________________________________________________

VI vstovi(const VS& c){
    VI ret;
    FORC(i,c) ret.push_back(atoi(c[i].c_str()));
    return ret;
}

//______________________________________________________________________________________________________________________

VI stovi(const string& s,string t=" "){
    return vstovi(split(s,t));
}

//______________________________________________________________________________________________________________________

VVI vstovvi(VS vs)
{
    VVI ret;
    FORC(i, vs)
    {
        VS t = split(vs[i]);
        VI r;
        FORC(j,t) r.push_back(toVal<int>(t[j]));
        ret.push_back(r);
    }
    return ret;
}

//______________________________________________________________________________________________________________________

enum Day { Sunday = 0, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday };
char* szDays[] = { "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" };

enum Month { January = 1, February, March, April, May, June, July, August, September, October, November, December };
int Months[] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
char* szMonths[] = { "None", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" };

bool IsLeap(int y) { return (y % 4 == 0 && y % 100 != 0 || y % 400 == 0) ? true : false; }

//______________________________________________________________________________________________________________________

// abs() doesn't work for long long that's why i have used max
template<typename T> T GCD(const T& a, const T& b) { return a == 0 ? std::max<T>(b, -b) : GCD<T>(b % a, a); }

template<typename T> T LCM(const T& a, const T& b) { return a * b == 0 ? 0 : a * b / GCD<T>(a, b); }

template<typename T> T GCD(const vector<T>& V)
{
    if (!V.size()) return -1;
    T ret(V[0]);
    for (int i = 1; i < (int) V.size(); ++i) ret = GCD(ret, V[i]);
    return ret;
}

template<typename T> T LCM(const vector<T>& V)
{
    if (!V.size()) return -1;
    T ret(V[0]);
    for (int i = 1; i < (int) V.size(); ++i) ret = LCM(ret, V[i]);
    return ret;
}

//______________________________________________________________________________________________________________________

int seconds(string time)
{
    int hh, mm, ss;
    sscanf (time.c_str(), "%d:%d:%d", &hh, &mm, &ss); 
    int ret = hh * 3600 + mm * 60 + ss;
    return ret;
}

//______________________________________________________________________________________________________________________

template<typename T> T Reverse(T N) {
    T ret = 0;
    while (N > 0) {
        ret = ret * 10 + (N % 10);
        N /= 10;
    }
    return ret;
}

template<typename T> bool IsPalindrome(T N) {
    return N == Reverse(N);
}

bool IsPalindrome(const string& s) {
    int N = s.size();
    FOR (i, N >> 1) if (s[i] != s[N - i - 1]) return false;
    return true;
}

bool IsPalindrome(const string& s, int l, int r) {
	int N = (r - l + 1) / 2;
	FOR(i, N) if (s[l + i] != s[r - i]) return false;
	return true;
}

//______________________________________________________________________________________________________________________

string time(int seconds)
{
    int hh = seconds / 3600;
    int remain = seconds % 3600;
    int mm = remain / 60;
    int ss = remain % 60;
    char str[24]="";
    sprintf (str, "%02d:02d:%02d", hh, mm, ss);
    return str;
}

//______________________________________________________________________________________________________________________

VD vstovd(VS  vs){VD ret; FORC(i,vs) ret.push_back(atof(vs[i].c_str())); return ret;}

//______________________________________________________________________________________________________________________

VVD vstovvd(VS  vs){VVD ret; FORC(i,vs) ret.push_back(vstovd(split(vs[i]))); return ret; }

//______________________________________________________________________________________________________________________

template<typename T> bool IsPrime(T n) {
	if (n == 2) return true;
	if (n <= 1 || n % 2 == 0) return false;
	T sqrtOfN = (T) sqrt(1.0 * n);
	for (T i = 3; i <= sqrtOfN; i += 2) if (n % i == 0) return false;
	return true;
}

//
// Ref: http://code.activestate.com/recipes/576559-fast-prime-generator/
// 
// Returns all the primes below _N_
//
template <typename T>
std::vector<unsigned long> GetPrimes(T N)
{
	std::vector<unsigned long> primes;
	char* sieve = new char[N / 8 + 1];
	memset(sieve, 0xFF, (N / 8 + 1) * sizeof(char));

	for (unsigned long x = 2; x <= N; ++x) {
		if (sieve[x / 8] & (0x01 << (x % 8))) {
			primes.push_back(x);
			// Is prime. Mark multiplicatives.
			for (unsigned long j = 2 * x; j <= N; j += x) {
				sieve[j / 8] &= ~(0x01 << (j % 8));
			}
		}
	}
	delete[] sieve;
	return primes;
}

//______________________________________________________________________________________________________________________

template <typename T> T FACT(const T& n) { return n == 0 ? 1 : n * FACT (n - 1); }

//______________________________________________________________________________________________________________________

int NCR (int n, int r)
{
    r = (r < n - r) ? r : n - r;
    int nom = 1, res = FACT(r);
    for( ; r > 0; --r) nom *= n--;
    return (nom / res);
}

long long NCR (int N, int R) {
    R = min(R, N - R);
    vector<int> vi1, vi2;
    FORN (i, 1, R) vi1.push_back(N - i + 1);
    FORN (i, 1, R) vi2.push_back(i);

    while (true) {
        bool valid = false;
        FORC (i, vi1) {
            FORC (j, vi2) {
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

    long long ret = 1;
    FORC (i, vi1) ret *= vi1[i];
    FORC (i, vi2) ret /= vi2[i];
    return ret;
}

//______________________________________________________________________________________________________________________

bool IsPerfectSQRT(int n) { if (n < 0) return false; int x = sqrt(1.0 * n); return x * x == n; }

//______________________________________________________________________________________________________________________

int NPR (int n, int r) { int ret = 1; for (int i = n - r + 1; i <= n; ++i) ret *= i; return ret; }

//______________________________________________________________________________________________________________________

template<class T> void UNQ (T& x) { sort(ALL(x)); x.resize(unique(ALL(x)) - x.begin()); }

//______________________________________________________________________________________________________________________
//LongestCommonSubsequence-LCS

int a[100][100];
FORN (i, 1, m)
FORN (j, 1, n)
if (X[i - 1] == Y[j - 1]) a[i][j] = a[i - 1][j - 1] + 1;
else a[i][j] = max (a[i - 1][j], a[i][j - 1]);

string backTrack (string& X, string& Y, int i, int j)
{
    if (i==0 || j==0)                return "";
    else if (X[i - 1] == Y[j - 1])        return backTrack (X, Y, i - 1, j - 1) + X[i - 1];
    else 
    {
        if (a[i][j - 1] > a[i - 1][j])    return backTrack (X, Y, i, j - 1);
        else return backTrack (X, Y, i - 1, j);
    }
}

class LongestCommonSubsequence
{
    string x, y;
    vector< vector<int> > a;

public:

    LongestCommonSubsequence(string _x, string _y) : x(_x), y(_y) {}

    vector< vector<int> > GetLCSArray()
    {
        a = vector< vector<int> > (x.length() + 1, vector<int> (y.length() + 1));
        for (int i = 1; i < x.size() + 1; ++i)
        for (int j = 1; j < y.size() + 1; ++j)
            a[i][j] = (x[i - 1] == y[j - 1] ? a[i - 1][j - 1] + 1 : max(a[i - 1][j], a[i][j - 1]));
        return a;
    }

    string BackTrack(int i, int j)
    {
        if (i == 0 || j == 0) return "";
        if (x[i - 1] == y[j - 1]) return BackTrack(i - 1, j - 1) + x[i - 1];
        if (a[i][j - 1] > a[i - 1][j]) return BackTrack(i, j - 1);
        return BackTrack(i - 1, j);
    }

    string BackTrack()
    {
        return BackTrack(x.size() + 1, y.size() + 1);
    }
};

// LCS of Array of Numbers
    // Determine an LCS of (1, 0, 0, 1, 0, 1, 0, 1) and (0, 1, 0, 1, 1, 0, 1, 1, 0)
    int a[] = { 1, 0, 0, 1, 0, 1, 0, 1 };
    int b[] = { 0, 1, 0, 1, 1, 0, 1, 1, 0 };
    VI va(ALL_ARRAY(a)), vb(ALL_ARRAY(b));

    vector < vector<int> > vvi(va.size() + 1, vector<int>(vb.size() + 1, 0));

    FORN (i, 1, va.size()) FORN (j, 1, vb.size())
        vvi[i][j] = (a[i - 1] == b[j - 1] ? vvi[i - 1][j - 1] + 1 : max(vvi[i - 1][j], vvi[i][j - 1]));

    FORC (i, vvi) { FORC (j, vvi[i]) cout << setw(3) << vvi[i][j]; cout << endl; }

    VI ret;

    for (int i = va.size(), j = vb.size(); i > 0 && j > 0; )
    {
        if (va[i - 1] == vb[j - 1])
        {
            ret.push_back(va[i - 1]);
            --i; --j;
        }
        else
        {
            vvi[i][j - 1] > vvi[i - 1][j] ? --j : --i ;
        }
    }
    reverse(ALL(ret));
    FORC (i, ret) cout << ret[i] << ", "; cout << endl;

//______________________________________________________________________________________________________________________

// Longest Increasing Subsequence
template<typename T> vector<int> LongestIncreasingSubsequence(const vector<T>& V)
{
    vector<int> best(V.size(), 1);
    for (int i = 0; i < V.size(); ++i)
        for (int j = 0; j < i; ++j) 
            if (V[i] >= V[j]) best[i] = max (best[i], 1 + best[j]);
    return best;
}

//______________________________________________________________________________________________________________________
// Floyd-Warshall Algorithm

    FOR (k, N)
        FOR (i, N)
        FOR (j, N)
        adj[i][j] = min (adj[i][j], adj[i][k] + adj[k][j]);

//______________________________________________________________________________________________________________________

template<class T> T reverse(T n){T ret=0;while (n>0){ ret = ret*10+(n%10); n/=10; }    return ret;}

//______________________________________________________________________________________________________________________
// Shortest Path algorithm
struct Node 
{
    int r, c;    int cost;

    Node(int _r, int _c, int _cost):r(_r), c(_c), cost(_cost) {}
    Node() {}
    bool operator<(const Node& N) const    { return cost > N.cost;    }
};

int dr[] = {2, -2, -2,  2, 1,  1, -1, -1};
int dc[] = {1,  1, -1, -1, 2, -2, -2,  2};

VS board;
int R, C;

struct Node 
{
    int r, c;    int cost;
    Node(int _r, int _c, int _cost) : r(_r), c(_c), cost(_cost) {}
    Node() {}
    bool operator < (const Node& N) const    { return cost > N.cost;    }
};

int doit (int si, int sj)
{
    int visit[10][10];
    int cost[10][10];    
    memset (visit, 0, sizeof(visit));
    FOR(i,10) FOR(j,10) cost[i][j] = 987654321;
    priority_queue <Node> pq;
    Node N (si, sj, 0);
    pq.push (N);
    while (!pq.empty())
    {
        N = pq.top(); pq.pop();
        
        if (visit[N.r][N.c]) continue;
        visit[N.r][N.c] = 1;
        cost[N.r][N.c] = N.cost;

        FOR (i, 8)
        {
            int r = N.r + dr[i];
            int c = N.c + dc[i];
            if (r >= 0 && r < R && c >= 0 && c < C && visit[r][c] == 0)
                pq.push(Node(r, c, N.cost + 1));
        }
    }
    int ret=0;
    FOR(i,R) FOR(j,C) if(board[i][j]!='.' && (i!=si || j!=sj))
    {
        int d = board[i][j]-'0';
        if(cost[i][j] < 987654321) ret += (cost[i][j] + d - 1) / d;
        else return -1;
    }
    return ret;
}


class CollectingRiders {
public:
    int minimalMoves(vector <string>);
};

int CollectingRiders::minimalMoves(vector <string> board) {
    int ret=INT_MAX;
    ::board = board;
    ::R = board.size();
    ::C = board[0].size();

    if (R<2||C<2) return -1;
    FOR (r, R) FOR (c, C)
    //if (board[r][c] != '.')
    {
        int res = doit (r, c);
        if (res != -1) ret = min (ret, res);
    }
    if (ret == INT_MAX) return -1;
    return ret;
}

//______________________________________________________________________________________________________________________
// LineIntersection

class Point
{
public:
    double x, y;
    Point(double _x=0.0f, double _y=0.0f) : x(_x), y(_y) {}
};    
enum IntersectResult { PARALLEL, COINCIDENT, NOT_INTERESECTING, INTERESECTING };
class LineSegment
{
public:
    Point begin;    Point end;
    LineSegment(const Point& b, const Point& e) : begin(b), end(e) {}
    LineSegment(double x1, double y1, double x2, double y2):begin(x1, y1), end(x2, y2) {}
};

IntersectResult IntersectLines(const LineSegment& L1, const LineSegment& L2, Point& intersection = *(new Point()))
{
    double denom =    ((L2.end.y - L2.begin.y)*(L1.end.x - L1.begin.x)) - 
                    ((L2.end.x - L2.begin.x)*(L1.end.y - L1.begin.y));
    double nume_a =    ((L2.end.x - L2.begin.x)*(L1.begin.y - L2.begin.y)) - 
                    ((L2.end.y - L2.begin.y)*(L1.begin.x - L2.begin.x));
    double nume_b = ((L1.end.x - L1.begin.x)*(L1.begin.y - L2.begin.y)) - 
                    ((L1.end.y - L1.begin.y)*(L1.begin.x - L2.begin.x));

    if(denom == 0.0f)
    {
        if(nume_a == 0.0f && nume_b == 0.0f) return COINCIDENT;
        return PARALLEL;
    }

    double ua = nume_a / denom;
    double ub = nume_b / denom;

    if(ua >= 0.0f && ua <= 1.0f && ub >= 0.0f && ub <= 1.0f)
    {
        // Get the intersection point.
        intersection.x = L1.begin.x + ua*(L1.end.x - L1.begin.x);
        intersection.y = L1.begin.y + ua*(L1.end.y - L1.begin.y);
        return INTERESECTING;
    }
    return NOT_INTERESECTING;
}
IntersectResult IntersectLines (const Point& p0, const Point& p1, 
                                const Point& p2, const Point& p3, Point& intersection = *(new Point()))
{
    LineSegment linesegment0(p0, p1);
    LineSegment linesegment1(p2, p3);
    return IntersectLines(linesegment0, linesegment1, intersection);
}

IntersectResult IntersectLines (double x1, double y1, double x2, double y2,
                                double x3, double y3, double x4, double y4, Point& intersection = *(new Point()))
{
    LineSegment linesegment0(x1, y1, x2, y2);
    LineSegment linesegment1(x3, y3, x4, y4);
    return IntersectLines(linesegment0, linesegment1, intersection);
}

//______________________________________________________________________________________________________________________
// NQueens

const int N = 8;
int a[N];
bool check (int r, int c)
{
    for (int i=0; i<r; ++i)
    if (c==a[i] || abs(r-i)==abs(c-a[i])) return false;
    return true;
}

void print ()
{
    for (int i=0; i<N; ++i)    cout << "(" << i << ", " << a[i] << ")   ";
    cout << endl;
}

void NQueens (int n = 0)
{
    for (int i = 0; i < N; ++i)
    if (check (n, i))
    {
        a[n] = i;
        if (n == N-1) print();
        else NQueens (n + 1);
    }
}

//______________________________________________________________________________________________________________________
// Fractional Structure

struct Fractional
{
    int numer, denom;

    Fractional (int n=0, int d=1)
    {
        numer = n;
        if (numer == 0) denom = 1;
        else
        {
            denom = d;
            if (denom < 0) { numer=-numer; denom=-denom; } 
            int g = GCD (numer, denom);
            numer/=g; denom/=g;
        }
    }

    Fractional operator + (const Fractional& O)
    { return Fractional (numer*O.denom+denom*O.numer, denom*O.denom);}

    Fractional operator - (const Fractional& O)
    { return Fractional (numer*O.denom-denom*O.numer, denom*O.denom);}

    Fractional operator * (const Fractional& O)
    { return Fractional (numer*O.numer, denom*O.denom);}

    Fractional operator / (const Fractional& O)
    { return Fractional (numer*O.denom, denom*O.numer);}

    bool operator < (const Fractional& O)
    { return numer*O.denom-denom*O.numer<0;}
};


struct Fraction {
    int m_N;        // Numerator;
    int m_D;        // Denominator;

    Fraction(int n = 0, int d = 1) {
        if ((m_N = n) == 0) { m_D = 1; }
        else {
            if ((m_D = d) < 0) { m_N = -m_N; m_D = -m_D; }
            int g = GCD(m_N, m_D);
            m_N /= g; m_D /= g;
        }
    }

    int GCD(const int& a, const int& b) { return a == 0 ? max(b, -b) : GCD(b % a, a); }

    Fraction operator + (const Fraction& O) { return Fraction(m_N * O.m_D + O.m_N * m_D, m_D * O.m_D); }

    Fraction operator - (const Fraction& O) { return Fraction(m_N * O.m_D - O.m_N * m_D, m_D * O.m_D); }

    Fraction operator * (const Fraction& O) { return Fraction(m_N * O.m_N, (m_D * O.m_D)); }

    Fraction operator / (const Fraction& O) { return Fraction(m_N * O.m_D, (m_D * O.m_N)); }

    bool operator < (const Fraction& O) { return m_N * O.m_D < m_D * O.m_N; }

    void Display() const {
        cout << m_N << " / " << m_D << " = " << 1. * m_N / m_D << endl;
    }
};

ostream& operator << (ostream& out, const Fraction& f) { f.Display(); return out; }

//______________________________________________________________________________________________________________________
//    SubStrings

    string s("Lokesh");    
    for (int i = 0; i < s.size(); ++i)
    for (int j = i; j < s.size(); ++j)
        cout << s.substr (i, j - i + 1) << endl;

    // decreasing order in length
    for (int len = s.size(); len > 0; --len)
    for (int i = 0; i <= s.size() - len; ++i)
        cout << s.substr (i, len) << endl;


//______________________________________________________________________________________________________________________

bool ASubsetOfB (const string& A, const string& B)
{
    for(int i = 0; i < A.size(); ++i)
        if (B.find(A[i]) == string::npos) return false;
    return true;
}

//______________________________________________________________________________________________________________________

bool ASubsetOfB (const unsigned int A, const unsigned int B) { if ((A & B) == A) return true; return false; }

//______________________________________________________________________________________________________________________

int BitCount (int n)
{
    int ret = 0;
    while (n > 0) { ++ret; n = n & (n-1); }
    return ret;
}

template<typename T> int DigitCount(T N) { return N ? (int)(log10(1. * max(N, -N)) + 1) : 0; }

//______________________________________________________________________________________________________________________

bool isPerfectSQRT(int n) { if (n < 0) return false; int x = sqrt(1.0 * n); return x * x == n; }
template<typename T>
bool QuadraticRoots(T a, T b, T c, pair<T, T>& p)
{
    if(!isPerfectSQRT(b*b-4*a*c)) return false;
    int x = sqrt(1.0*(b*b-4*a*c));
    if ((-b+x)%(2*a)==0) p.first=(-b+x)/(2*a); else p.first=INT_MAX;
    if ((-b-x)%(2*a)==0) p.second=(-b-x)/(2*a); else p.second=INT_MAX;
    return true;
}

//______________________________________________________________________________________________________________________

// Matrix Determinant
int DET (vector<vector<int> > vvi)
{
    int ret = 0;
    int N = (int) vvi.size();
    if(N == 1)return vvi[0][0];
    FOR(i, N)
    {
        int x = ((i%2)?-1:1) * vvi[0][i];
        vector< vector<int> > tvvi;
        for(int j = 1; j < N; ++j) 
        {
            vector<int> vi;
            FOR(k, N) if(k != i) vi.push_back(vvi[j][k]);
            tvvi.push_back(vi);
        }
        ret += x*DET(tvvi);
    }
    return ret;
}

// Number of Spanning Trees in a Graph.
int NumSpanningTrees (const vector< vector<int> >& vvi)
{
    int N = (int) vvi.size();
    vector< vector<int> > t(N,vector<int>(N,0));
    FOR(i, N) FOR(j, N) if (i != j) t[i][j]=(vvi[i][j]>0)?-1:0;
    FOR(i, N) t[i][i] = count(ALL(t[i]), -1);
    vector< vector<int> > x(N-1, vector<int>(N-1));
    FOR(i, N-1) FOR(j, N-1) x[i][j] = t[i][j];
    return DET(x);
}

//______________________________________________________________________________________________________________________
// Factors
vector<int> GetFactors(long long n)
{
    vector<int> ret;
    for (long long i = 1; i * i <= n; ++i) if (n % i == 0) {
        ret.push_back(i);
        ret.push_back(n/i);
    }
    return ret;
}
//______________________________________________________________________________________________________________________
// PrimeFactors
template<typename T>
void GetPrimeFactors(T n, map<int, int>& mp) {
    mp.clear();
    int sqrtOfN = sqrt((double)n);
    for (T x = 2; x <= sqrtOfN; ++x) {
        while (n % x == 0) {
            mp[x]++;
            n /= x;
        }
    }
    if (n != 1) mp[n]++;
}

template<typename T>
vector<T> GetPrimeFactors(T n, bool duplicates=false)
{
	vector<T> ret;
	T sqrtOfN = sqrt((double)n);
	for (T x = 2; x <= sqrtOfN; ++x) {
		if (duplicates) {
			while (n % x == 0) {
				ret.push_back((T)x);
				n /= x;
			}
		}
		else {
			if (n % x == 0) { ret.push_back((T)x); }
			while (n % x == 0) { n /= x; }
		}
	}
	if (n != 1) ret.push_back(n);
	return ret;
}


template<typename T>
vector<int> GetPrimeFactors(T n)
{
    vector<int> ret;
    int sqrtOfN = sqrt((double)n);
    for (T x = 2; x <= sqrtOfN; ++x) {
        while (n % x == 0) {
            ret.push_back((int) x);
            n /= x;
        }
    }
    if (n != 1) ret.push_back(n);
    return ret;
}

//
//    Euler's Totient function :-
//        f(n) [sometimes called the phi function], is used to determine
//        the number of numbers less than n which are relatively prime to n.
//    For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, f(9)=6.
//
int Phi(int n)
{
    int ret = 1;
    typedef map<int, int> Map_I2I;
    Map_I2I mp;
    GetPrimeFactors(n, mp);
    for (Map_I2I::iterator it = mp.begin(); it != mp.end(); ++it)
        ret *= (it->first - 1) * pow(1. * it->first, it->second - 1);
    return ret;
}

//______________________________________________________________________________________________________________________
// Kruskal's Minimum Spanning Tree
vector< pair<int, int> > SpanningTree_Kruskals (vector< vector<int> > a)
{
    struct Node
    {
        int i, j, cost;
        Node () {}
        Node (int _i, int _j, int _cost):i(_i), j(_j), cost(_cost){}
        bool operator < (const Node& oth) const
        {
            return cost > oth.cost;
        }
    };
    priority_queue<Node> q;
    int n = (int) a.size(), cc = 0;
    FOR(i, n) FOR(j, n)    if (i < j && a[i][j] != -1)    q.push(Node(i, j, a[i][j]));
    vector< set<int> > sts(n);
    FOR(i, n) sts[i].insert(i);
    vector< pair<int, int> > ret;
    while(!q.empty())
    {
        Node no = q.top(); q.pop();
        int i = no.i; int j = no.j;
        int s1, s2;
        for(int k = 0; k < (int)sts.size(); ++k) 
        { 
            if (sts[k].count(i)) s1 = k; 
            if (sts[k].count(j)) s2 = k; 
        }
        if (s1 == s2) continue;
        cc++;
        sts[s1].insert(ALL(sts[s2])); sts[s2].clear();
        ret.push_back(make_pair(i,j));
        if (cc == n-1) break;
    }
    if (cc != n-1) { ret.clear(); }
    return ret;
}
//______________________________________________________________________________________________________________________
// Prims Minimum Spanning Tree
vector< pair<int, int> > SpanningTree_Prims (vector< vector<int> > a)
{
    int N = (int) a.size();
    vector< pair<int, int> > ret, edges;
    FOR(i, N) FOR(j, N) if(i < j && a[i][j] != -1) edges.push_back(make_pair(i, j));
    set<int> vertices, verticesNew; 
    FOR(i, N) vertices.insert(i);
    verticesNew.insert(0);
    while (verticesNew != vertices)
    {
        pair<int, int> newedge;
        int cost = INT_MAX;
        FORC(i, edges)
        {
            int u = edges[i].first, v = edges[i].second, c = a[u][v];
            if (find(ALL(verticesNew), u) == verticesNew.end() || 
                find(ALL(verticesNew), v) != verticesNew.end())
            {
                swap(u, v);
                if (find(ALL(verticesNew), u) == verticesNew.end() || 
                    find(ALL(verticesNew), v) != verticesNew.end()) continue;
            }
            if (cost > c) newedge.first = u, newedge.second = v,     cost = a[u][v];
        }
        ret.push_back(newedge);
        verticesNew.insert(newedge.second);
        vector< pair<int, int> >::iterator it = find(ALL(edges), newedge);
        if (it == edges.end())
        {
            swap(newedge.first, newedge.second);
            it = find(ALL(edges), newedge);
        }        
        edges.erase(it);
    }
    return ret;
}
//______________________________________________________________________________________________________________________
//Members of vals must be distinct
//Based on C++ next_permutation function
int[] nextperm(int[] vals) {
   int i =  vals.length-1;
   while (true) {
      int ii =  i;
      i--;
      if (vals[i] < vals[ii]) {
         int j = vals.length;
         while (vals[i] >= vals[--j]);
            int temp = vals[i];  //Swap
            vals[i] = vals[j]; 
            vals[j] = temp;
         int begin = ii, end = vals.length-1;
         while (end>begin) {
               int stemp = vals[end];   //Swap
               vals[end] = vals[begin]; 
               vals[begin] = stemp;
            end--; begin++;
         }   
         return vals;
      } else if (vals[i] == vals[0]) {
         int begin = 0, end = vals.length-1;
         while (end>begin) {
               int stemp = vals[end];   //Swap
               vals[end] = vals[begin]; 
               vals[begin] = stemp;
            end--; begin++;
         }   
         return vals;
      }
   }
}
//______________________________________________________________________________________________________________________

double AreaOfTrianlge(double x1, double y1, double x2, double y2, double x3, double y3)
{
    return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2));
}

double LengthOfLine (double x, double y, double a, double b)
{
    return _hypot(x - a, y - b);
}

double AreaOfTriangle (double A, double B, double C)
{
    double S = (A + B + C) / 2.0;
    return sqrt (S * (S - A) * (S - B) * (S - C));
}

double LengthOfLine (double x1, double y1, double z1, double x2, double y2, double z2)
{    return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) + (z1-z2)*(z1-z2)); }

double AreaOfTriangle (double x1, double y1, double z1, 
                       double x2, double y2, double z2, 
                       double x3, double y3, double z3)
{
    double A = LengthOfLine(x1, y1, z1, x2, y2, z2);
    double B = LengthOfLine(x2, y2, z2, x3, y3, z3);
    double C = LengthOfLine(x3, y3, z3, x1, y1, z1);
    double S = (A + B + C) / 2.0;
    return sqrt (S * (S - A) * (S - B) * (S - C));
}

//______________________________________________________________________________________________________________________

// N u m b e r s
string toRadix(int value, int radix) {
    string s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string ret = "";
    while (value > 0) {
        int r = value % radix;
        ret = s[r] + ret;
        value /= radix;
    }
    return ret.emtpy() ? "0" : ret;
}

template <typename T> int GetDigitsSum(T N) {
	return N > 0 ? N % 10 + GetDigitsSum(N / 10) : 0;
}

int GetDigitsSum(const string& S) {
	int ret = 0;
	for (int i = 0; i < S.size(); ++i) ret += S[i] - '0';
	return ret;
}

int numcmp(const string& a, const string& b)
{
	string sa = TrimLeft(a, "0");
	string sb = TrimLeft(b, "0");

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

std::string Sub(std::string x, std::string y)
{
	using std::max;
	bool		minusSign = false;
	std::string ret;
	int			carry = 0;

	x = TrimLeft(x, "0");
	y = TrimLeft(y, "0");

	if (numcmp(x, y) < 0) {
		std::swap(x, y);
		minusSign = true;
	}

	size_t len = max(x.size(), y.size());
	if (x.size() < len) x.insert(0, std::string(len - x.size(), '0'));
	if (y.size() < len) y.insert(0, std::string(len - y.size(), '0'));
	ret.resize(len);

	for (int i = len - 1; i >= 0; --i) {
		// Convert char to int using: ch & 0xf
		int sum = (x[i] & 0xf) - (y[i] & 0xf) + carry;
		if (sum < 0) { carry = -1; sum += 10; }
		else		 { carry = 0; }
		sum = sum % 10;
		ret[i] = sum | 0x30;	// Convert digit to char
	}

	if (minusSign) ret.insert(ret.begin(), '-');
	return ret;
}

void sum(string x, string y, string& ret) {
	int carry = 0, sum;
	int len = max(x.size(), y.size());
	if (x.size() < len) x.insert(0, string(len - x.size(), '0'));
	if (y.size() < len) y.insert(0, string(len - y.size(), '0'));
	ret.resize(len);

	for (int i = len - 1; i >= 0; --i) {
		sum		= (x[i] & 0xf) + (y[i] & 0xf) + carry;
		carry	= (sum > 9 ? 1 : 0);
		sum		= sum % 10;
		ret[i]	= sum | 0x30;
	}

	if (carry) ret.insert(ret.begin(), '1');
}


void sum2(const string& x, const string& y, string& ret)
{
	int carry = 0, t;
	int lenx = x.size();
	int leny = y.size();
	int len = max(lenx, leny);
	ret.resize(len);
	int i, ix, iy;

	for (i = len - 1, ix = lenx - 1, iy = leny - 1; ix >= 0 && iy >= 0; --ix, --iy, --i) {
		t = (x[ix] & 0xf) + (y[iy] & 0xf) + carry;
		carry = (t > 9) ? 1 : 0;
		t = t % 10;
		ret[i] = (t | 0x30);
	}

	if (ix >= 0 || iy  >= 0) {
		const string& rem = (ix >= 0 ? x : y);
		int ixy = (ix >= 0 ? ix : iy);
		for (; ixy >= 0; --ixy, --i) {
			t = (rem[ixy] & 0xf) + carry;
			carry = (t > 9) ? 1 : 0;
			t = t % 10;
			ret[i] = (t | 0x30);
		}
	}

	if (carry) ret.insert(ret.begin(), '1');
}

string sub(string x, string y)
{
    int len = max(x.size(), y.size());
    if (x.size() < len) x = string(len - x.size(), '0') + x;
    if (y.size() < len) y = string(len - y.size(), '0') + y;
    string sign = "";
    if (x < y) { swap(x,  y); sign = "-"; }

    string ret = "";
    for (int i = len - 1; i >= 0; --i)
    {
        if (x[i] >= y[i])
        {
            ret = char(x[i] - y[i] + '0') + ret;
        }
        else
        {
            ret = char(10 + x[i] - y[i] + '0') + ret;
            x[i - 1] -= 1;
        }
    }
    return sign + ret.substr(ret.find_first_not_of("0"));
}

string pow(int a, int b) {
    string ret = toString<int>(a);
    FOR (i, b - 1) {
        string t = ret;
        FOR (j, a - 1) ret = sum(ret, t);
    }
    return ret;
}

//
// Returns the sum of x and y
//
std::string Sum(std::string x, std::string y)
{
	using std::max;
	std::string	ret;
	int			carry = 0;
	int			sum;
	size_t		len;

	// Trim leading spaces
	x = TrimLeft(x, "0");
	y = TrimLeft(y, "0");

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

	for (int i = len - 1; i >= 0; --i) {
		// Convert char to int using: ch & 0xf
		sum		= (x[i] & 0xf) + (y[i] & 0xf) + carry;
		carry	= (sum > 9 ? 1 : 0);
		sum		= sum % 10;
		ret[i]	= sum | 0x30;	// Convert digit to char
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
	bool		minusSign = false;
	std::string ret;
	int			carry = 0;

	// Trim leading spaces
	x = TrimLeft(x, "0");
	y = TrimLeft(y, "0");

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

	for (int i = len - 1; i >= 0; --i) {
		// Convert char to int using: ch & 0xf
		int sum = (x[i] & 0xf) - (y[i] & 0xf) + carry;
		if (sum < 0) { carry = -1; sum += 10; }
		else		 { carry = 0; }
		sum = sum % 10;
		ret[i] = sum | 0x30;	// Convert digit to char
	}

	// Remove leading zeros (007)
	ret = TrimLeft(ret, "0");
	if (ret.empty()) return "0";

	if (minusSign) ret.insert(ret.begin(), '-');
	return ret;
}

//______________________________________________________________________________________________________________________

long long Concat(long long n1, long long n2) {
    int n2Len = n2 ? (int)(log10(1. * max(n2, -n2)) + 1) : 0;
    long long P = 1;
    n1 = n1 * pow(10.0, n2Len);
    n1 += (n2 % 10); n2 /= 10;
    while (n2 > 0) {
        n1 += (n2 % 10) * (P *= 10);
        n2 /= 10;
    }
    return n1;
}

//______________________________________________________________________________________________________________________

struct Point
{
    int x;
    int y;

    Point(int _x, int _y) : x(_x), y(_y) {}
};

struct Circle
{
    int x;
    int y;
    int r;

    Circle(int _x, int _y, int _r) : x(_x), y(_y), r(_r) {}
};

bool PointIsInsideCircle(const Point& p, const Circle& c)
{
    int dx = p.x - c.x;
    int dy = p.y - c.y;
    double dr = sqrt((double)(dx * dx + dy * dy));
    return dr <= (double) c.r;
}

//______________________________________________________________________________________________________________________

bool MakeMask(int N, int& mask) {
    int r = 0;
    while (N > 0) {
        int r = N % 10;
        if (r == 0) return false;
        if (mask & 1 << (r - 1)) return false;
        mask |= (1 << (r - 1));
        N /= 10;
    }
    return true;
}

bool GetMask_0to9(int N, int& mask) {
    int r = 0; mask = 0;
    while (N > 0) {
        int r = N % 10;
        if (mask & 1 << r) return false;
        mask |= (1 << r);
        N /= 10;
    }
    return true;
}

//______________________________________________________________________________________________________________________

// ::Numbers

template<typename T> int GetNumberOfDigits(T N) { return N ? (int)(log10(1. * max(N, -N)) + 1) : 0; }

	bool IsPowerOf(Int64 n, Int64 p) {
		Int32 pr = p % 10;
		Int32 nr = n % 10;
		switch (pr) {
		case 0: if (nr == 0)									return true; break;
		case 1: if (nr == 1)									return true; break;
		case 2: if (nr == 2 || nr == 4 || nr == 6 || nr == 8)	return true; break;
		case 3: if (nr == 1 || nr == 3 || nr == 7 || nr == 9)	return true; break;
		case 4: if (nr == 4 || nr == 6)							return true; break;
		case 5: if (nr == 5)									return true; break;
		case 6: if (nr == 6)									return true; break;
		case 7: if (nr == 1 || nr == 3 || nr == 7 || nr == 9)	return true; break;
		case 8: if (nr == 2 || nr == 4 || nr == 6 || nr == 8)	return true; break;
		case 9: if (nr == 1 || nr == 9)							return true; break;
		}
		return false;
	}

//______________________________________________________________________________________________________________________

template<typename T> T Replace(T N, int d1, int d2) {
    T ret    = 0;
    int sign = N > 0 ? 1 : -1, t;
    N = max(N, -N);
    while (N > 0) {
        ret = ret * 10 + ((t = N % 10) == d1 ? d2 : t);
        N /= 10;
    }
    return sign * Reverse(ret);
}

// This method is faster than the above method.
template<typename T> T Replace(T N, int d1, int d2) {
    T ret    = 0, P = 1;
    int len  = N ? (int)(log10(1. * max(N, -N)) + 1) : 0;
    int sign = N > 0 ? 1 : -1, t;
    N = max(N, -N);
    ret = (t = N % 10) == d1 ? d2 : t; N /= 10;
    for (int i = 1; i < len; ++i) {
        ret += ((t = N % 10) == d1 ? d2 : t) * (P *= 10);
        N /= 10;
    }
    return sign * ret;
}

template<typename T> bool Replace(T N, int d1, int d2, int& ret) {
    T TN = N, P = 1; ret = 0;
    int len  = N ? (int)(log10(1. * max(N, -N)) + 1) : 0;
    int sign = N > 0 ? 1 : -1, t;
    N = max(N, -N);
    ret = (t = N % 10) == d1 ? d2 : t; N /= 10;
    for (int i = 1; i < len; ++i) {
        ret += ((t = N % 10) == d1 ? d2 : t) * (P *= 10);
        N /= 10;
    }
    return sign * ret != TN;
}

template<typename T> T ReplaceALL(T N, int d1, int d2) {
    T ret    = 0, P = 1;
    int len  = N ? (int)(log10(1. * max(N, -N)) + 1) : 0;
    int sign = N > 0 ? 1 : -1, t;
    N = max(N, -N);
    ret = (t = N % 10) == d1 ? d2 : t; N /= 10;
    for (int i = 1; i < len; ++i) {
        ret += ((t = N % 10) == d1 ? d2 : t) * (P *= 10);
        N /= 10;
    }
    return sign * ret;
}

//______________________________________________________________________________________________________________________

template<typename T> bool IsPermutation(T x, T y) {
    int A[10] = {0};
    while (x > 0) { A[x % 10]++; x /= 10; }
    while (y > 0) { if (--A[y % 10] < 0) return false; y /= 10; }
    FOR(i, 10) if (A[i] != 0) return false;
    return true;
}

//______________________________________________________________________________________________________________________

typedef enum { KeyUnknown = -1, KeyUp, KeyDown, KeyEnter, KeyInsert, KeyDelete, KeyEsc } Keys;

Keys GetKey() {
    int ch[2] = { 0 };
    
    ch[0] = _getch();
    if (ch[0] == 0x1b)    return KeyEsc;
    if (ch[0] == 0xd)    return KeyEnter;
    ch[1] = _getch();

    if (ch[1] == 0x48)    return KeyUp;
    if (ch[1] == 0x50)    return KeyDown;
    if (ch[1] == 0x52)    return KeyInsert;
    if (ch[1] == 0x53)    return KeyDelete;

    return KeyUnknown;
}

//______________________________________________________________________________________________________________________
// ::Geometry
double Slope(double x1, double y1, double x2, double y2) { return (y1 - y2) / (x1 - x2); }

bool IsParallel(double x1, double y1, double x2, double y2, double x3, double y3, double x4, double y4, double tolerance = 1e-9) {
    double y12 = y1 - y2, x12 = x1 - x2;
    double y34 = y3 - y4, x34 = x3 - x4;
    return (fabs(y12 * x34 - y34 * x12) <= tolerance);
}

bool IsParallel(const pair<double, double>& pt1, const pair<double, double>& pt2,
                const pair<double, double>& pt3, const pair<double, double>& pt4, double tolerance = 1e-9) {
    double y12 = pt1.second - pt2.second, x12 = pt1.first - pt2.first;
    double y34 = pt3.second - pt4.second, x34 = pt3.first - pt4.first;
    return (fabs(y12 * x34 - y34 * x12) <= tolerance);    
}

bool IsPerpendicular(double x1, double y1, double x2, double y2, double x3, double y3, double x4, double y4, double tolerance = 1e-9) {
    double y12 = y1 - y2, x12 = x1 - x2;
    double y34 = y3 - y4, x34 = x3 - x4;
    return (fabs(x12 * x34 + y12 * y34) <= tolerance);
}

bool IsPerpendicular(const pair<double, double>& pt1, const pair<double, double>& pt2,
                const pair<double, double>& pt3, const pair<double, double>& pt4, double tolerance = 1e-9) {
    double y12 = pt1.second - pt2.second, x12 = pt1.first - pt2.first;
    double y34 = pt3.second - pt4.second, x34 = pt3.first - pt4.first;
    return (fabs(x12 * x34 + y12 * y34) <= tolerance);
}

bool IsRectangle(const vector<pair<double, double> >& v, double tolerance = 1e-9, bool pointsAreInOrder = true) {
    if (pointsAreInOrder) {
        if (!IsParallel(v[0], v[1], v[2], v[3]))        return false;
        if (!IsParallel(v[1], v[2], v[0], v[3]))        return false;
        if (IsPerpendicular(v[0], v[2], v[1], v[3]))    return false;
    }
    else {
        vector<pair<double, double> > tv(v);
        do {
            if (IsRectangle(tv, tolerance)) return true;
        } while (next_permutation(ALL(tv)));
        return false;
    }
    return true;
}

bool IsSquare(const vector<pair<double, double> >& v, double tolerance = 1e-9, bool pointsAreInOrder = true) {
    if (pointsAreInOrder) {
        if (!IsParallel(v[0], v[1], v[2], v[3]))        return false;
        if (!IsParallel(v[1], v[2], v[0], v[3]))        return false;
        if (!IsPerpendicular(v[0], v[2], v[1], v[3]))    return false;
    }
    else {
        vector<pair<double, double> > tv(v);
        do {
            if (IsSquare(tv, tolerance)) return true;
        } while (next_permutation(ALL(tv)));
        return false;
    }
    return true;
}

//______________________________________________________________________________________________________________________
// ::PRINTing / ::Trace

//
// Trace function
//  Use DbgView from Sysinternals to intercept the
//  printouts.
//
void lgTrace(const char* format, ...) {
    va_list tArgs;
    int     iLen;
    char*   szOut;

    // Anything to print
    if (!format) return;

    // Get length of output string
    va_start(tArgs, format);
    iLen = _vscprintf(format, tArgs) + 1;

    // Create output string
    szOut = new char[iLen];
    if (szOut == NULL) {
        OutputPRINTString("lgTrace: Memory allocation problem\n");
        return;
    }

    // Print
    vsprintf_s(szOut, iLen, format, tArgs);
    OutputPRINTString(szOut);

    // Free output string
    delete [] szOut;
}


void _lgtrace(const TCHAR *format, ...)
{
	TCHAR buffer[1024];
	va_list argptr;
	va_start(argptr, format);
	wvsprintf(buffer, format, argptr);
	va_end(argptr);
	OutputDebugString(buffer);
}

#define LGDBGVIEWSTR		_T("[DbgView] %s: ")
#define LGDBGVIEWARG		_T(__FUNCTION__)
#define LGTRACE(fmt, ...)	_lgtrace(LGDBGVIEWSTR fmt, LGDBGVIEWARG, __VA_ARGS__)

//______________________________________________________________________________________________________________________

struct CVerbose	{
	FILE* m_fp;
	int   m_nNameLength;
	char  m_szFmt[24];
	char  m_szSep[9];

	CVerbose(FILE* _fp = stdout, int _nNameLength = 24, char* szSep = ":")
		: m_fp(_fp)
		, m_nNameLength(_nNameLength)
	{
		strcpy_s(m_szSep, _countof(m_szSep), szSep);
		BuildFormatString();
	}

	void Print(const _TCHAR* sName, const _TCHAR* sFormat, ...)
	{
		_ftprintf(m_fp, m_szFmt, sName);

		va_list tArgs;
		va_start(tArgs, sFormat);
		_vftprintf(m_fp, sFormat, tArgs);

		_ftprintf(m_fp, "%s", "\n");
		fflush(m_fp);

		return;
	}

private:

	void BuildFormatString() {
		sprintf_s(m_szFmt, _countof(m_szFmt), "%%%ds %s ", m_nNameLength, m_szSep);
	}
};

// -----------------------------------------------------
// Method:    	verbose
// Description: Print a message in verbose mode
//				
// Returns:  	void
// Parameter: 	const _TCHAR * sName
// Parameter: 	const _TCHAR * sFormat
// Parameter: 	...
// -----------------------------------------------------
void isVerbose(const _TCHAR* sName, const _TCHAR* sFormat, ...)
{
	_ftprintf(stdout, "%21s : ", sName);

	va_list tArgs;
	va_start(tArgs, sFormat);
	_vftprintf(stdout, sFormat, tArgs);

	_ftprintf(stdout, "%s", "\n");
	fflush(stdout);

	return;
}

void isVerbose(FILE* fp, const char* sName, const char* sFormat, ...)
{
	fprintf_s(fp, "%27s : ", sName);

	va_list tArgs;
	va_start(tArgs, sFormat);
	vfprintf(fp, sFormat, tArgs);

	fprintf(fp, "%s", "\n");
	fflush(fp);

	return;
}

//______________________________________________________________________________________________________________________
// ::String / ::Strings

char AND(char x, char y) { return (x == '1' && y == '1' ? '1' : '0'); }
char OR(char x, char y) { return (x == '1' || y == '1' ? '1' : '0'); }
char XOR(char x, char y) { return (x == y ? '0' : '1'); }

string AND(const string& s1, const string& s2) {
	string ret;
	FORC (i, s1) ret += AND(s1[i], s2[i]);
	return ret;
}

string OR(const string& s1, const string& s2) {
	string ret;
	FORC (i, s1) ret += OR(s1[i], s2[i]);
	return ret;
}

string XOR(const string& s1, const string& s2) {
	string ret;
	FORC (i, s1) ret += XOR(s1[i], s2[i]);
	return ret;
}

// Return the number of occurrences of string fnd in string s
int Count(const string& s, const string& fnd, bool overlap = true) {
    int ret = 0, pos = 0, fndSz = fnd.size();
    while (pos != string::npos) {
        pos = s.find(fnd, pos);
        if (pos != string::npos) {
            ++ret;
            pos += (overlap ? 1 : fndSz);
        }
    }
    return ret;
}

//______________________________________________________________________________________________________________________
::Sort

// Frequency sort
template<typename ContainerDataType, typename ContainerType>
struct FrequencySort {
	map<ContainerDataType, int> m_frequency;

	FrequencySort(const ContainerType& c) {
		ContainerType::const_iterator it;
		for (it = c.begin(); it != c.end(); ++it) {
			m_frequency[*it]++;
		}
	}

	bool operator()(const ContainerDataType& i, const ContainerDataType& j) {
		if (m_frequency[i] == m_frequency[j]) {
			return i < j;
		}
		return m_frequency[i] < m_frequency[j];
	}
};

    // example:
	// string s("aaabbc");
	// sort(ALL(s), FrequencySort<char, string>(s));
    // output: "cbbaaa"

//______________________________________________________________________________________________________________________

template<typename T>
std::string GetTypeName(const T& obj) {
	const std::type_info& ti = typeid(obj);
	return ti.name();
}


template<typename T>
std::string GetClassName(const T& obj) {
	std::string name = GetTypeName(obj);
	if (name.find("struct") == 0 || name.find("class") == 0) {
		return name.substr(name.find(' ') + 1);
	}
	return name;
}


//______________________________________________________________________________________________________________________

template <typename T> stringstream& operator >> (stringstream& ss, std::vector<T>& v) {
	v.clear();
	T val;
	while (ss >> val) { v.push_back(val); }
	return ss;
}

template <typename T> fstream& operator >> (fstream& fs, std::vector<T>& v) {
	v.clear();
	std::string line;
	std::getline(fs, line);
	// just return if line is empty.
	size_t p = line.find_first_not_of(" ", 0);
	if (p == std::string::npos) return fs;
	size_t q = line.find_last_not_of(" ");
	line = line.substr(p, q - p + 1);
	stringstream ss(line);
	T val;
	while (ss >> val) { v.push_back(val); }
	return fs;
}

struct StreamReader {
	std::string		m_FilePath;
	std::fstream	m_fs;

	StreamReader(std::string path) : m_FilePath(path), m_fs(path) {
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

	template <typename T> bool Read(T& t) {
		return (bool)(m_fs >> t);
	}

	template <typename T> bool Read(vector<vector<T>>& t) {
		t.clear();
		vector<T> vt;
		while (m_fs >> vt) {
			if (vt.empty()) return true;
			t.push_back(vt);
		}
		return true;
	}

	template<class T> T ToVal(const std::string& s) { T ret; istringstream iss(s); iss >> ret; return ret; }

	std::string Trim(const std::string& str, std::string seps = " ")
	{
		if (str.empty()) return str;
		size_t p = str.find_first_not_of(seps);
		if (p == std::string::npos) return "";
		size_t q = str.find_last_not_of(seps);
		return str.substr(p, q - p + 1);
	}

	template <typename T> bool Read(vector<T>& vt, const std::string& seps) {
		vt.clear();
		std::string line;
		ReadLine(line);
		line = Trim(line);
		for (size_t p = 0, q = 0; q != string::npos; p = q) {
			p = line.find_first_not_of(seps, p);
			if (p == string::npos) break;
			q = line.find_first_of(seps, p);
			vt.push_back(ToVal<T>(line.substr(p, q - p)));
		}
		return true;
	}

	template <typename T> bool Read(vector<vector<T>>& vvt, const string& seps) {
		vvt.clear();
		vector<T> vt;
		while (Read(vt, seps)) {
			if (vt.empty()) return true;
			vvt.push_back(vt);
		}
		return true;
	}

	template <typename T> T Read() {
		T t;
		if (!(m_fs >> t)) {
			string typeName = GetTypeName(t);
			throw std::exception(std::string("failed to read <" + typeName + ">.").c_str());
		}
		return t;
	}

	bool IsEOF() { return m_fs.eof(); }

	operator bool() { return !m_fs.eof(); }
};

//______________________________________________________________________________________________________________________
// ::Roman

// 
// I = 1
// V = 5
// X = 10
// L = 50
// C = 100
// D = 500
// M = 1000
// 
// Rules:
//	(1) Only I, X, and C can be used as the leading numeral in part of a subtractive pair.
//	(2) I can only be placed before V and X.
//	(3) X can only be placed before L and C.
//	(4) C can only be placed before D and M.
// 

struct Roman {
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

    static long Convert(string romanNumeral) {
        long ret = 0;
        char prev = '\0';
        FOREACH(ch, romanNumeral) {
            ch = toupper(ch);
            ret += Get(ch);
            if (prev && Get(prev) < Get(ch)) {
                ret -= (Get(prev) << 1);
            }
            prev = (ch == 'I' || ch == 'X' || ch == 'C') ? ch : '\0';
        }
        return ret;
    }

    static string Convert(long decimal) {
        const int N = 13;
        long   dec[N] = { 1000, 900,  500, 400,  100,  90,  50,  40,   10,   9,    5,   4,    1  };
        string num[N] = {  "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };
        string numeral;

        FOR(i, N) {
            while (decimal >= dec[i]) {
                decimal -= dec[i];
                numeral.append(num[i]);
            }
        }

        return numeral;
    }
};

//______________________________________________________________________________________________________________________

//
// Simple expression evaluator
// Ref: http://www.strchr.com/expression_evaluator
// (c) Peter Kankowski, 2007. http://smallcode.weblogs.us mailto:kankowski@narod.ru
// 
class ExprEval {
	// Error codes
	enum EXPR_EVAL_ERR {
		EEE_NO_ERROR		= 0,
		EEE_PARENTHESIS		= 1,
		EEE_WRONG_CHAR		= 2,
		EEE_DIVIDE_BY_ZERO	= 3
	};

	typedef char EVAL_CHAR;

private:

	EXPR_EVAL_ERR	_err;
	EVAL_CHAR*		_err_pos;
	int				_paren_count;

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

//______________________________________________________________________________________________________________________

std::string FormatSize(double size, int precision=2)
{
	char buf[1024];
	//static char* units[] = { "bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB" };
	string units = "KMGTPEZYB";
	int index = -1;
	while (size >= 1024) {
		++index;
		size /= 1024.;
	}
	
	char fmt[32];

	if (index == -1) {
		sprintf_s(fmt, "%%.%df bytes", precision);
		sprintf_s(buf, fmt, size);
	}
	else {
		sprintf_s(fmt, "%%.%df %%cB", precision);
		sprintf_s(buf, fmt, size, units[index]);
	}
	return buf;
}

//______________________________________________________________________________________________________________________

struct mynumpunct : std::numpunct<char> {
	std::string do_grouping() const { return "\03"; }
	char do_thousands_sep() const { return ','; }
};

template<typename T>
std::string FormatGrouping(T value)
{
	std::locale loc(std::cout.getloc(), new mynumpunct());
	std::ostringstream oss;
	oss.imbue(loc);
	oss << value;
	return oss.str();
}

//______________________________________________________________________________________________________________________

std::string GetCurrentDateTime() {
	char szDateTime[26] = { 0 };

	time_t startedClock;
	time(&startedClock);
	errno_t err;
	struct tm startedInfo;
	err = localtime_s(&startedInfo, &startedClock);

	if (!err) {
		err = asctime_s(szDateTime, _countof(szDateTime), &startedInfo);
		if (err) {
			sprintf_s(szDateTime, "%s %d", __TIME__, __DATE__);
		}
		else {
			szDateTime[24] = '\0';
		}
	}

	return szDateTime;
}

struct ScopedTimer
{
	ScopedTimer() {
		QueryPerformanceCounter(&m_tStartTime);
		m_Started = GetCurrentDateTime();
		printf_s("Started : %s\n", m_Started.c_str());
	}

	~ScopedTimer() {
		QueryPerformanceCounter(&m_tStopTime);
		QueryPerformanceFrequency(&m_tFrequency);
		m_Elapsed = (double)(m_tStopTime.QuadPart - m_tStartTime.QuadPart) / (double)m_tFrequency.QuadPart;

		m_Ended = GetCurrentDateTime();
		printf_s("Ended   : %s\n", m_Ended.c_str());
		printf_s("Elapsed : %f\n", m_Elapsed);
	}

private:

	LARGE_INTEGER	m_tStartTime;
	LARGE_INTEGER	m_tStopTime;
	LARGE_INTEGER	m_tFrequency;
	std::string		m_Started;
	std::string		m_Ended;
	double			m_Elapsed;
	std::string		m_Name;
};

//______________________________________________________________________________________________________________________

std::string GetCurrentDateTime() {
	char szDateTime[26] = { 0 };

	time_t startedClock;
	time(&startedClock);
	errno_t err;
	struct tm startedInfo;
	err = localtime_s(&startedInfo, &startedClock);

	if (!err) {
		err = asctime_s(szDateTime, _countof(szDateTime), &startedInfo);
		if (err) {
			sprintf_s(szDateTime, "%s %d", __TIME__, __DATE__);
		}
		else {
			szDateTime[24] = '\0';
		}
	}

	return szDateTime;
}

struct ScopedTimer
{
	ScopedTimer() {
		QueryPerformanceCounter(&m_tStartTime);
		m_Started = GetCurrentDateTime();
		std::cout << "Started : " << m_Started << std::endl;
	}

	~ScopedTimer() {
		QueryPerformanceCounter(&m_tStopTime);
		QueryPerformanceFrequency(&m_tFrequency);
		m_Elapsed = (double)(m_tStopTime.QuadPart - m_tStartTime.QuadPart) / (double)m_tFrequency.QuadPart;

		m_Ended = GetCurrentDateTime();
		//std::cout << "Started : " << m_Started << std::endl;
		std::cout << "Ended   : " << m_Ended << std::endl;
		std::cout << "Elapsed : " << m_Elapsed << std::endl;
	}

private:

	LARGE_INTEGER	m_tStartTime;
	LARGE_INTEGER	m_tStopTime;
	LARGE_INTEGER	m_tFrequency;
	std::string		m_Started;
	std::string		m_Ended;
	double			m_Elapsed;
};

//______________________________________________________________________________________________________________________

template<typename T>
struct SubsetSum {
    std::vector<T> vi;

    SubsetSum(const std::vector<T> &_vi) {
        this->vi = _vi;
    }

    bool solve(T sum) {
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
        if (false) {
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
};

//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
//______________________________________________________________________________________________________________________
#pragma warning(disable:4786)
#pragma warning(disable:4244) // conversion double - int
#pragma warning(disable:4267) // conversion size_t - int
#pragma warning(disable:4018) // signed/unsigned comparision

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std; 
//______________________________________________________________________________________________________________________
typedef vector< int >               VI;
typedef vector< string >            VS;
typedef vector< double >            VD;
typedef vector< vector< double > >  VVD;
typedef vector< vector< string > >  VVS;
typedef vector< vector< int > >     VVI;
//______________________________________________________________________________________________________________________
#define MPI 3.14159265358979323846264338327950288419716939937510
//______________________________________________________________________________________________________________________
#define STR_(x)                     #x
#define STR(x)                      STR_(x)
#define SIZE(C)                     C.size() 
#define ALL(C)                      (C).begin(), (C).end() 
#define SIZE_ARRAY(A)               (sizeof(A) / sizeof(A[0]))
#define ALL_ARRAY(A)                (A), (A) + SIZE_ARRAY(A)
#define FOR(i, N)                   for (int i = 0; i < (int)(N); ++i)
#define FORC(i, C)                  for (int i = 0; i < (int)(C).size(); ++i)
#define FORN(i, x, n)               for (int i = x; i <= (int)(n); ++i)
#define FOREACH(T, it, C)           for (T::iterator it = (C).begin(); it != (C).end(); ++it)
#define DEG_TO_RAD(deg)             ((deg * 2.0 * MPI) / 360.0)
#define RAD_TO_DEG(rad)             ((360.0 / (2.0 * MPI)) * rad)
#define TIME(t)                     clock_t t = clock()
#define TIME_DIFF(t1, t2)           (1.0 * abs(t2 - t1) / CLOCKS_PER_SEC)
#define TRACE(x)                    cout << (x) << endl
#define PRINT(x)                    cout << #x << " = " << (x) << endl
#define    CRLF                        cout << endl
#define FIND(c, v)                  (find(c.begin(), c.end(), v) != c.end())
//______________________________________________________________________________________________________________________
#define FILE_OPEN(fs, path)                                            \
    fstream fs(path);                                                \
    if (fs.is_open() == false) {                                    \
        cout << "file not opened" << endl;                            \
        exit(-1);                                                    \
    }                                                                \

#define	PRINT_TIME(exp)	{													\
	TIME(t1);																\
	exp;																	\
	TIME(t2);																\
	cout <<	STR(exp) <<	" :	" << TIME_DIFF(t1, t2) << "	s" << endl;			\
}																			\
    
template<typename T> ostream& operator << (ostream& out, const std::vector<T>& V) {
	if (V.empty()) return out;
	out << "{ " << V[0];
	for (int i = 1; i < (int)V.size(); ++i) out << ", " << V[i];
	out << " }";
	return out;
}

template<typename T1, typename T2>
ostream& operator << (ostream& out, const std::pair<T1, T2>& pr) {
	out << "(" << pr.first << ", " << pr.second << ")";
	return out;
}

template<typename TKey, typename TValue>
ostream& operator << (ostream& out, const std::map<TKey, TValue>& mp) {
	if (mp.empty()) return out;
	std::map<TKey, TValue>::const_iterator it = mp.begin();
#if 0
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

//______________________________________________________________________________________________________________________

/*    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    */
// ::Codeforces
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <string>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std; 

//______________________________________________________________________________________________________________________

typedef std::vector< int >               VI;
typedef std::vector< string >            VS;
typedef std::vector< double >            VD;
typedef std::vector< std::vector< double > >  VVD;
typedef std::vector< std::vector< string > >  VVS;
typedef std::vector< std::vector< int > >     VVI;

//______________________________________________________________________________________________________________________


#define STR_(x)                     #x
#define STR(x)                      STR_(x)

// C Macros
#define PRINT_INT(x)				printf_s("%s = [%d]\n", STR(x), x)
#define PRINT_UINT(x)				printf_s("%s = [%u]\n", STR(x), x)
#define PRINT_DBL(x)				printf_s("%s = [%f]\n", STR(x), x)
#define PRINT_STR(x)				printf_s("%s = [%s]\n", STR(x), x)
#define PRINT_DEC(x)				printf_s("%s = [%d]\n", STR(x), x)
#define PRINT_HEX(x)				printf_s("%s = [%#x]\n", STR(x), x)
#define PRINT_OCT(x)				printf_s("%s = [%#o]\n", STR(x), x)
#define PRINT_PTR(x)				printf_s("%s = [%#x]\n", STR(x), x)

#define SIZE(C)                     C.size() 
#define ALL(C)                      (C).begin(), (C).end() 
#define ARRAY_SIZE(A)               (sizeof(A) / sizeof(A[0]))
#define SIZE_ARRAY(A)               (sizeof(A) / sizeof(A[0]))
#define ALL_ARRAY(A)                (A), (A) + SIZE_ARRAY(A)

#define FOR(i, N)                   for (int i = 0; i < (int)(N); ++i)
#define FORC(i, C)                  for (int i = 0; i < (int)(C).size(); ++i)
#define FORN(i, x, n)               for (int i = x; i <= (int)(n); ++i)

#if _MSC_VER >= 1700	/* VisualStudio 2012, VC++ compiler */
#define FOREACH(x, C)               for (auto& x : C)
#else
#define FOREACH(T, it, C)           for (T::iterator it = (C).begin(); it != (C).end(); ++it)
#endif

#define DEG_TO_RAD(deg)             ((deg * 2.0 * MPI) / 360.0)
#define RAD_TO_DEG(rad)             ((360.0 / (2.0 * MPI)) * rad)
#define TRACE(x)                    std::cout << (x) << std::endl
#define PRINT(x)                    std::cout << #x << " = [" << (x) << "]" << std::endl
#define PRINT2(a, b)									\
	std::cout											\
		<< STR(a) << " = [" << (a) << "], "				\
		<< STR(b) << " = [" << (b) << "]" << std::endl

#define PRINT3(a, b, c)									\
	std::cout											\
		<< STR(a) << " = [" << (a) << "], "				\
		<< STR(b) << " = [" << (b) << "], "				\
		<< STR(c) << " = [" << (c) << "]" << std::endl

#define PRINT4(a, b, c, d)								\
	std::cout											\
		<< STR(a) << " = [" << (a) << "], "				\
		<< STR(b) << " = [" << (b) << "], "				\
		<< STR(c) << " = [" << (c) << "], "				\
		<< STR(d) << " = [" << (d) << "]" << std::endl

#define REDIRECTSTDOUT(filePath)                                        \
	printf_s("Redirecting stdout to \"%s\". @ Func : %s, Line : %d\n",  \
		filePath, __FUNCTION__, __LINE__);                              \
	freopen_s((FILE**)stdout, filePath, "w+t", stdout)

#define TIME(t)                     clock_t t = clock()

#define TIME_DIFF(t1, t2)           (1.0 * abs(t2 - t1) / CLOCKS_PER_SEC)

#define	PRINT_TIME(exp)	{														\
	TIME(t1);																	\
	exp;																		\
	TIME(t2);																	\
	std::string str = STR(exp);													\
	if (str.size() > 40) { str.resize(36); str += " ..."; }						\
	str += " [Line: #" STR(__LINE__) "]";										\
	std::cout <<	str <<	" : " << TIME_DIFF(t1, t2) << " s" << std::endl;	\
}

namespace {

template<typename T> ostream& operator << (ostream& out, const vector<T>& V) {
	if (V.empty()) return out;
	out << "{ " << V[0];
	for (int i = 1; i < (int)V.size(); ++i) out << ", " << V[i];
	out << " }";
	return out;
}

struct CStopWatch
{
	void timerStart() {
		QueryPerformanceCounter(&m_tStartTime);
	}

	double timerStop() {
		QueryPerformanceCounter(&m_tStopTime);
		QueryPerformanceFrequency(&m_tFrequency);

		return (double)(m_tStopTime.QuadPart - m_tStartTime.QuadPart) / (double)m_tFrequency.QuadPart;
	}

private:

	LARGE_INTEGER m_tStartTime;
	LARGE_INTEGER m_tStopTime;
	LARGE_INTEGER m_tFrequency;
};

} /* Anonymous namespace end */

int main()
{
#if defined(_DEBUG)
    freopen_s((FILE**) stdin, "ReadMe.txt", "r", stdin);
#endif

    return 0;
}

// ::Codeforces
