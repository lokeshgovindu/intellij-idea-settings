/*****************************************************************************/
/*                                                                           */
/*                  This is  Lokesh Govindu's header file.                   */
/*                                                                           */
/* - This is my C/C++ backup's header file.                                  */
/*                                                                           */
/*****************************************************************************/

/**
 * \file	LoGo.h
 *
 * \author	Lokesh Govindu
 * Contact: lokeshgovindu@gmail.com
 *
 * \brief 
 *
 * TODO:	long description
 *
 * \note
 */

#ifndef __LoGo_H__
#define __LoGo_H__

#define LGCHR(x)						#@x
#define LGSTR_(x)						#x
#define LGSTR(x)						LGSTR_(x)
#define LGCAT(x, y)						x##y

#pragma message("[INFO] *** Including [" __FILE__ "] header file at Line #" LGSTR(__LINE__) " ***")

/*****************************************************************************/

#include <tchar.h>
#include <io.h>
#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <stdarg.h>

#include <windows.h>

// C Macros
#define LGPRINT_INT(x)				printf_s("%s = [%d]\n",		LGSTR(x), x)
#define LGPRINT_UINT(x)				printf_s("%s = [%u]\n",		LGSTR(x), x)
#define LGPRINT_FLT(x)				printf_s("%s = [%f]\n",		LGSTR(x), x)
#define LGPRINT_DBL(x)				printf_s("%s = [%lf]\n",	LGSTR(x), x)
#define LGPRINT_STR(x)				printf_s("%s = [%s]\n",		LGSTR(x), x)
#define LGPRINT_DEC(x)				printf_s("%s = [%d]\n",		LGSTR(x), x)
#define LGPRINT_HEX(x)				printf_s("%s = [%#x]\n",	LGSTR(x), x)
#define LGPRINT_OCT(x)				printf_s("%s = [%#o]\n",	LGSTR(x), x)
#define LGPRINT_PTR(x)				printf_s("%s = [%#x]\n",	LGSTR(x), x)

/* Built-in data-types in C/C++ */

typedef signed char					Int8;
typedef signed short				Int16;
typedef signed int					Int32;
typedef signed long long			Int64;
typedef signed __int64				Int64;
typedef unsigned char				UInt8;
typedef unsigned short				UInt16;
typedef unsigned int				UInt32;
typedef unsigned long long			UInt64;
typedef unsigned __int64			UInt64;
typedef char						Char;
typedef float						Single;
typedef double						Double;

#if !defined(__cplusplus)
typedef unsigned char				Boolean;
#if !defined(MAX_STRING_LEN)	
#define MAX_STRING_LEN				256
#endif
typedef char						String[MAX_STRING_LEN];
#endif

/*****************************************************************************/

//-----------------------------------------------------------------------------
// C++ starts here!
//-----------------------------------------------------------------------------

#if defined(__cplusplus)

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
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <regex>

/*****************************************************************************/

#define LOGO_NS			LoGo
#define LOGO_NS_BEGIN	namespace LOGO_NS {
#define LOGO_NS_END		}
#define USE_LOGO_NS		using namespace LOGO_NS;

typedef bool									Boolean;

typedef std::vector<int>						VI;
typedef std::vector<unsigned long>				VUL;
typedef std::vector<unsigned long long>			VULL;
typedef std::vector<double>						VD;
typedef std::vector<std::vector<double>>		VVD;
typedef std::vector<std::vector<int>>			VVI;
typedef std::vector<Int32>						VInt32;
typedef std::vector<UInt32>						VUInt32;
typedef std::vector<Int64>						VInt64;
typedef std::vector<UInt64>						VUInt64;
typedef std::vector<long>						VL;
typedef std::vector<unsigned long>				VUL;

typedef std::vector<std::string>				VS;
typedef std::vector<std::wstring>				VWS;
typedef std::vector<std::vector<std::string>>	VVS;
typedef std::vector<std::vector<std::wstring>>	VVWS;

// ----------------------------------------------------------------------------
// UNICODE related stuff
// ----------------------------------------------------------------------------

#ifndef _UNICODE
typedef std::string					String;
#define tcout						std::cout
typedef std::string					tstring;
#else /* _UNICODE */
typedef std::wstring				String;
#define tcout						std::wcout
typedef std::wstring				tstring;
#endif	// _UNICODE


typedef std::vector<tstring>		VTS;

/*****************************************************************************/

#define MPI							3.14159265358979323846264338327950288419716939937510

/*****************************************************************************/

#define SIZE(C)						C.size()
#define ALL(C)						(C).begin(), (C).end()
#define ARRAY_SIZE(A)				(sizeof(A) / sizeof(A[0]))
#define SIZE_ARRAY(A)				(sizeof(A) / sizeof(A[0]))
#define ALL_ARRAY(A)				(A), (A) + ARRAY_SIZE(A)

//#define FOREACH(T, it, C)			for (T::iterator it = (C).begin(); it != (C).end(); ++it)

#if _MSC_VER >= 1700	/* VisualStudio 2012, VC++ compiler */
#define FOR(i, n)					for (decltype(n) i = 0; i < (n); ++i)
#define FORR(i, n)					for (decltype(n) i = n - 1; i >= 0; --i)
#define FORC(i, C)					for (size_t i = 0; i < (C).size(); ++i)
#define FORN(i, x, n)				for (decltype(n) i = x; i <= (n); ++i)
#define FORU(i, x, n)				for (decltype(N) i = x; i <= (n); ++i)
#define FORD(i, n, x)				for (decltype(x) i = n; i >= (x); --i)
#define FORX(i, a, b, inc)			for (decltype(b) i = a; i <= (b); i += (inc))
#define FOREACH(x, C)               for (auto& x : C)
#else
#define FOR(i, n)					for (int i = 0; i < (n); ++i)
#define FORR(i, n)					for (int i = n - 1; i >= 0; --i)
#define FORC(i, C)					for (int i = 0; i < (C).size(); ++i)
#define FORN(i, x, n)				for (int i = x; i <= (n); ++i)
#define FORU(i, x, n)				for (int i = x; i <= (n); ++i)
#define FORD(i, n, x)				for (int i = n; i >= (x); --i)
#define FORX(i, a, b, inc)			for (int i = a; i <= (b); i += (inc))
#define FOREACH(T, it, C)           for (T::iterator it = (C).begin(); it != (C).end(); ++it)
#endif

#define FORI(N)						FOR(i, N)
#define FORJ(N)						FOR(j, N)
#define FORK(N)						FOR(k, N)

#define FORRI(N)					FORR(i, N)
#define FORRJ(N)					FORR(j, N)
#define FORRK(N)					FORR(k, N)


#define DEG_TO_RAD(deg)				((deg * 2.0 * MPI) / 360.0)
#define RAD_TO_DEG(rad)				((360.0 / ( 2.0 * MPI)) * rad)

#define TIME(t)						clock_t t = clock()
#define TIME_DIFF(t1, t2)			(1.0 * abs(t2 - t1) / CLOCKS_PER_SEC)

#define SORT(C)						sort(ALL(C))
#define FIND(c, v)					(find(c.begin(), c.end(), v) != c.end())
#define SWAP(x, y)					(x) ^= (y) ^= (x) ^= (y)

#define LINE						tcout << "---------------------------------------------------------------------------------------------------" << endl
#define	CRLF						tcout << endl
#define READ_NUMBER(num)			cin >> num;
#define READ_STRING(S)				\
	cin.ignore();					\
	getline(cin, S);

#define LGTRACE(a)								std::cout << (a) << std::endl
#define LGTRACE1(a)								std::cout << (a) << std::endl

#define LGTRACE2(a, b)														\
	std::cout << (a) << ", " << (b) << std::endl

#define LGTRACE3(a, b, c)													\
	std::cout << (a) << ", " << (b) << ", " << (c) << std::endl

#define LGTRACE4(a, b, c, d)												\
	std::cout << (a) << ", " << (b) << ", " << (c) << ", " << (d) << std::endl

#define LGTRACE5(a, b, c, d, e)												\
	std::cout << (a) << ", " << (b) << ", " << (c) << ", " << (d) << ", "	\
			  << (e) << std::endl

#define LGTRACE6(a, b, c, d, e, f)											\
	std::cout << (a) << ", " << (b) << ", " << (c) << ", " << (d) << ", "	\
			  << (e) << ", " << (f) << std::endl

#define LGTRACE7(a, b, c, d, e, f, g)										\
	std::cout << (a) << ", " << (b) << ", " << (c) << ", " << (d) << ", "	\
			  << (e) << ", " << (f) << ", " << (g) << std::endl

#define LGTRACE8(a, b, c, d, e, f, g, h)									\
	std::cout << (a) << ", " << (b) << ", " << (c) << ", " << (d) << ", "	\
			  << (e) << ", " << (f) << ", " << (g) << ", " << (h) << std::endl

#define LGTRACE9(a, b, c, d, e, f, g, h, i)									\
	std::cout << (a) << ", " << (b) << ", " << (c) << ", " << (d) << ", "	\
			  << (e) << ", " << (f) << ", " << (g) << ", " << (h) << ", "	\
			  << (i) << std::endl

#define LGPRINT(x)	std::cout << LGSTR(x) << " = [" << (x) << "]" << std::endl
#define LGPRINT1(x)	std::cout << LGSTR(x) << " = [" << (x) << "]" << std::endl

#define LGPRINT2(a, b)										\
	std::cout												\
		<< LGSTR(a) << " = [" << (a) << "], "				\
		<< LGSTR(b) << " = [" << (b) << "]" << std::endl

#define LGPRINT3(a, b, c)									\
	std::cout												\
		<< LGSTR(a) << " = [" << (a) << "], "				\
		<< LGSTR(b) << " = [" << (b) << "], "				\
		<< LGSTR(c) << " = [" << (c) << "]" << std::endl

#define LGPRINT4(a, b, c, d)								\
	std::cout												\
		<< LGSTR(a) << " = [" << (a) << "], "				\
		<< LGSTR(b) << " = [" << (b) << "], "				\
		<< LGSTR(c) << " = [" << (c) << "], "				\
		<< LGSTR(d) << " = [" << (d) << "]" << std::endl

#define LGWPRINT(x)		std::wcout << LGSTR(x) << " = [" << (x) << "]" << std::endl
#define LGWPRINT1(x)	std::wcout << LGSTR(x) << " = [" << (x) << "]" << std::endl

#define LGWPRINT2(a, b)										\
	std::cout												\
		<< LGSTR(a) << " = [" << (a) << "], "				\
		<< LGSTR(b) << " = [" << (b) << "]" << std::endl

#define LGWPRINT3(a, b, c)									\
	std::cout												\
		<< LGSTR(a) << " = [" << (a) << "], "				\
		<< LGSTR(b) << " = [" << (b) << "], "				\
		<< LGSTR(c) << " = [" << (c) << "]" << std::endl

#define LGWPRINT4(a, b, c, d)								\
	std::cout												\
		<< LGSTR(a) << " = [" << (a) << "], "				\
		<< LGSTR(b) << " = [" << (b) << "], "				\
		<< LGSTR(c) << " = [" << (c) << "], "				\
		<< LGSTR(d) << " = [" << (d) << "]" << std::endl

/*****************************************************************************/

//
// Open file for reading
//
#define LGFILE_OPEN(fs, path)					\
	fstream fs(path);							\
	if (fs.is_open() == false) {				\
		cout << "file not opened" << endl;		\
	}


//
// Redirect stdout to a text file.
//
#define LGREDIRECTSTDOUT(filePath)											\
	printf_s("Redirecting stdout to [%s], @ Func : [%s], Line : [%d]\n",	\
		filePath, __FUNCTION__, __LINE__);									\
	freopen_s((FILE**)stdout, filePath, "w+t", stdout);

//
// Redirect stdin to a text file.
//
#define LGREDIRECTSTDIN(filePath)											\
	printf_s("Redirecting stdin to [%s], @ Func : [%s], Line : [%d]\n",		\
		filePath, __FUNCTION__, __LINE__);									\
	freopen_s((FILE**)stdin, filePath, "r", stdin);

//
// Redirect stdout back to console.
//
#define LGREDIRECTSTDOUTTOCONSOLE											\
	freopen_s((FILE**)stdout, "con", "w", stdout);							\
	printf_s("Redirecting stdout to [CON], @ Func : [%s], Line : [%d]\n",	\
		__FUNCTION__, __LINE__);

#ifndef _LGPRINT_TIME_
#define _LGPRINT_TIME_
#define LGPRINT_TIME(exp)													\
{																			\
	TIME(t1);																\
	exp;																	\
	TIME(t2);																\
	cout << LGSTR(exp) << " : " << TIME_DIFF(t1, t2) << " s" << endl;		\
}
#endif


LOGO_NS_BEGIN

/**
 * Return the type of object.
 *
 * GetTypeName(24)		=> [int]
 * GetTypeName(24.9)	=> [double]
 * GetTypeName('x')		=> [char]
 * GetTypeName("LoGo")	=> [char const [5]]
 * 
 * char* szName = "LoGo";
 * GetTypeName(szName)	=> [char *]
 * 
 * struct tagStudent { };
 * GetTypeName(new tagStudent)	=> [struct tagStudent *]
 * GetTypeName(tagStudent())	=> [struct tagStudent]
 * 
 * class tagStudent { };
 * GetTypeName(new tagStudent)	=> [class tagStudent *]
 * GetTypeName(tagStudent())	=> [class tagStudent]
 * 
 * \param[in]	obj		Object
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
 * GetClassName(new tagStudent)	=> [tagStudent *]
 * GetClassName(tagStudent())	=> [tagStudent]
 *
 * \param[in]	obj		Object
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
 */
std::ostream& operator << (std::ostream& out, const std::wstring& wstr)
{
	std::wcout << wstr;
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


/**
 * template specialization for std::vector<std::string>.
 * Print vector elements on stdout.
 */
template<>
std::ostream& operator << (std::ostream& out, const std::vector<std::string>& V) {
	if (V.empty()) return out;
	out << "{ " << "\"" << V[0] << "\"";
	for (size_t i = 1; i < V.size(); ++i) {
		out << ", " << "\"" << V[i] << "\"";
	}
	out << " }";
	return out;
}


/**
 * Print std::pair<T1, T2> on stdout as shown below.
 * 
 * std::pair<int, int> pt = make_pair<int, int>(24, 9);
 * cout << pt << endl;
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
bool IsLeap(Int32 y) { return (y % 4 == 0 && y % 100 != 0 || y % 400 == 0); }


/**
 *	Splits and returns the request type of std::vector.
 */
template <typename T>
std::vector<T> Split(const std::string& s, const std::string& seps = " ")
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
 *	\brief Splits the string into vector of strings.
 */
std::vector<std::string> Split(const std::string& s, const std::string& seps = " ")
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
 *	\brief This is almost similar to Split method, but separator is space here.
 *	
 *	Extracts vector of type T from string stream.
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
 *	\brief Read and returns the vector of elements from fstream (file, single line).
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
	stringstream ss(line);
	T val;
	while (ss >> val) { v.push_back(val); }
	return fs;
}


/**
 *	\brief Returns the prime factors and their count in std::map.
 *	
 *	\param[in]	n	Number, for which you want to get primes.
 *	\param[out]	mp	Map container for storing primes and their count.
 *	
 *	\sa	std::vector<T> GetPrimeFactors(T n, bool duplicates=false)
 *	
 *	\code
 *	std::map<int, int> mp;
 *	GetPrimeFactors(36, mp);
 *	LGPRINT(mp);
 *
 *	Output: mp = [{ 2: 2, 3: 2 }]
 *	\endcode
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
 *	\brief This function computes the prime factors of given number \a n.
 *	
 *	\param[in]	n			Number, for which you want to get prime factors.
 *	\param[in]	duplicates	Allow duplicates in output vector.
 *	
 *	\return	Returns the vector of prime factors for the given number \a n.
 *	
 *	\sa	void GetPrimeFactors(T n, std::map<int, int>& mp)
 *	
 *	\code
 *	GetPrimeFactors(36, true)  => [{ 2, 2, 3, 3 }]
 *	GetPrimeFactors(36, false) => [{ 2, 3 }]
 *	\endcode
 */
template<typename T>
std::vector<T> GetPrimeFactors(T n, bool duplicates=false)
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
 *	\brief Returns the all prime factors count of a given number.
 *	
 *	\param[in]	n			Number to which you want to get the prime factors count.
 *	\param[in]	duplicates	Count duplicates also.
 *	
 *	\return		Return the prime factors count of a given number.
 *	
 *	\sa	void GetPrimeFactors(T n, std::map<int, int>& mp)
 *	\sa	std::vector<T> GetPrimeFactors(T n, bool duplicates=false)
 *
 *	\code
 *	GetPrimeFactorsCount(36, true)  => [4]
 *	GetPrimeFactorsCount(36, false) => [2]
 *	\endcode
 */
template<typename T>
unsigned long GetPrimeFactorsCount(T n, bool duplicates=false)
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
 *	\brief Returns the factors of a given number in std::vector.
 *	
 *	\param[in]	n	Number for which you want to get the factors.
 *	
 *	\return		Returns the factors of a given number \a n in std::vector.
 *	
 *	\code
 *	GetAllFactors(36) => { 1, 36, 2, 18, 3, 12, 4, 9, 6 }
 *	\endcode
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
 *	\brief Returns the number of factors of a given number.
 *	
 *	\param[in]	n	Number for which you want to get the factors.
 *	
 *	\return		Returns the number of factors of a given number \a n.
 *	
 *	\sa	std::vector<T> GetAllFactors(T n)
 *	
 *	\code
 *	GetAllFactorsCount(36) => 9
 *	\endcode
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
 *	\brief Checks if the given number if prime or not.
 *	
 *	\param[in]	n	Number

 *	\return True if given number \a n is prime, false otherwise.
 *	
 *	\sa std::vector<unsigned long> GetPrimes(T N)
 */
template<typename T>
bool IsPrime(T n)
{
	if (n == 2)					return true;
	if (n <= 1 || n % 2 == 0)	return false;
	T sqrt_n = static_cast<T>(sqrt(1.0 * n));
	for (T i = 3; i <= sqrt_n; i += 2) if (n % i == 0) return false;
	return true;
}


/**
 *	\brief Computes the primes below \a N
 *	
 *	\param[in]	N	Number
 *	
 *	\return Number of primes below \a N in a vector.
 *	
 *	\sa bool IsPrime(T n)
 *	
 *	\ref http://code.activestate.com/recipes/576559-fast-prime-generator/
 */
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


int CountRectangles(int W, int H, bool includeSquares = false) {
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

double sign(const fPoint2D& p1, const fPoint2D& p2, const fPoint2D& p3)
{
	return (p1.X - p3.X) * (p2.Y - p3.Y) - (p2.X - p3.X) * (p1.Y - p3.Y);
}

bool PointInTriangle(const fPoint2D& pt, const fPoint2D& v1, const fPoint2D& v2, const fPoint2D& v3)
{
	bool b1, b2, b3;

	b1 = sign(pt, v1, v2) < 0.0f;
	b2 = sign(pt, v2, v3) < 0.0f;
	b3 = sign(pt, v3, v1) < 0.0f;

	return ((b1 == b2) && (b2 == b3));
}


/**
 *	\brief Compute the reverse of given number \a N
 *	
 *	\return Reverse of the given number \a N
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
template <typename T> bool HasAllOddDigits(T n)
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
template <typename T> bool HasAllEvenDigits(T n)
{
	for (; n > 0; n /= 10) {
		if (n & 1) {
			return false;
		}
	}
	return true;
}

//
// Returns the sum of x and y
//
void Sum(std::string x, std::string y, std::string& ret)
{
	using std::max;
	int carry = 0, sum;
	size_t len = max(x.size(), y.size());
	if (x.size() < len) x.insert(0, std::string(len - x.size(), '0'));
	if (y.size() < len) y.insert(0, std::string(len - y.size(), '0'));
	ret.resize(len);

	for (int i = len - 1; i >= 0; --i) {
		sum		= (x[i] & 0xf) + (y[i] & 0xf) + carry;
		carry	= (sum > 9 ? 1 : 0);
		sum		= sum % 10;
		ret[i]	= sum | 0x30;
	}

	if (carry) ret.insert(ret.begin(), '1');
}


//
// Contain all the digits 1 to 9, but not necessarily in order.
// 
template <typename T> bool IsPandigital(const T& N)
{
	const int SZ = 10;
	char check[SZ] = { 1, 0 };
	for (T n = N; n > 0; n /= 10) check[n % 10] = 1;
	FOR(i, SZ) if (!check[i]) return false;
	return true;
}


bool IsPandigital(const std::string& s, int begin = 0, int end = -1)
{
	const int SZ = 10;
	char check[SZ] = { 1, 0 };
	size_t N = s.size();
	if (end == -1) end = N - 1;
	if ((end - begin + 1) < 9 || s.size() < 9) return false;
	FORN(i, begin, end) check[s[i] - '0'] = 1;
	FOR(i, (int)SZ) if (!check[i]) return false;
	return true;
}


//template <> bool IsPandigital<char*>(const char*& s) {
bool IsPandigital(const char* s) {
	const int SZ = 10;
	char check[SZ] = { 1, 0 };
	int len = strlen(s);
	FOR(i, len) check[s[i] - '0'] = 1;
	FOR(i, (int)SZ) if (!check[i]) return false;
	return true;
}


template <class T>
void UNQ(T& x)
{
	sort(ALL(x));
	x.resize(unique(ALL(x)) - x.begin());
}

//
// :::Numbers / :::Numeric
//

/**
 *	\brief	Return number of 1s in \a n in binary.
 *			
 *	\param[in]	n	Number
 *	
 *	\return		Return number of 1s in \a n in binary.
 *	
 *	\sa GetBinaryCardinality
 */
template <typename T>
int BitCount(T n)
{
	int ret = 0;
	while (n > 0) { ++ret; n = n & (n - 1); }
	return ret;
}


/**
 *	\brief	Return the minimum number of bits required to represent \a n
 *			as a binary number.
 *			
 *	\param[in]	n	Number
 *	
 *	\return		Minimum #bits required to represent \a n in a binary number.
 *	
 *	\sa BitCount
 */
template <typename T>
int BinaryCardinality(T n)
{
	return log2(n) + 1;
}


/**
 *	\brief	Returns the number of digits in a given \a N in its decimal
 *			representation.
 *			
 *	\param[in]	N	Number
 *	
 *	\return Number of digits in given number \a N
 *	
 *	\sa	BitCount
 *	\sa BinaryCardinality
 */
template <typename T>
int DigitCount(T N)
{
	return N ? (int)(log10(1. * max(N, -N)) + 1) : 0;
}

/**
 *	\brief Checks if A is subset of B
 *	
 *	\param[in]	A	First number
 *	\param[in]	B	Second number
 *	
 *	\return True if A is subset of B, otherwise False.
 */
bool ASubsetOfB(unsigned int A, unsigned int B)
{
	return (A & B) == A;
}


/**
 *	\brief Factorial of a given number \a n
 *	
 *	\return Factorial of a given number \a n
 */
template <typename T> T Factorial(const T& n)
{
	return n == 0 ? 1 : n * Factorial(n - 1);
}


/**
 *	\brief NCR of given numbers \a n and \a r.
 *	
 *	\param[in]	n	N value
 *	\param[in]	r	R value
 *	
 *	\return	NCR
 *	
 *	\code
 *	NCR(5, 0) = [1]
 *	NCR(5, 1) = [5]
 *	NCR(5, 2) = [10]
 *	NCR(5, 5) = [1]
 *	\endcode
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
 *	\brief Checks if the given number \a n is bouncy.
 *	
 *	Working from left-to-right if no digit is exceeded by the digit to its left
 *	it is called an increasing number; for example, 134468.
 *
 *	Similarly if no digit is exceeded by the digit to its right it is called a
 *	decreasing number; for example, 66420.
 *
 *	We shall call a positive integer that is neither increasing nor decreasing
 *	a "bouncy" number; for example, 155349.
 *
 *	\param[in]	n	Number
 *	
 *	\return	True if \a n is bouncy, otherwise False.
 *	
 *	\sa IsIncreasingNumber
 *	\sa IsStrictlyIncreasingNumber
 *	\sa IsDecreasingNumber
 *	\sa IsStrictlyDecreasingNumber
 *	
 *	\ref https://projecteuler.net/problem=112
 *	
 *	\code
 *	IsBouncy(155349) = [true]
 *	\endcode
 */
template <typename T>
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
 *	\brief Checks if the given number \a n is increasing or not.
 *	
 *	Working from left-to-right if no digit is exceeded by the digit to its left
 *	it is called an increasing number; for example, 134468.
 *	
 *	\param[in]	n	Number
 *	
 *	\return	True if \a n is increasing, otherwise False.
 *	
 *	\sa IsStrictlyIncreasingNumber
 *	\sa IsDecreasingNumber
 *	\sa IsStrictlyDecreasingNumber
 *	\sa IsBouncy
 *	
 *	\ref https://projecteuler.net/problem=112
 *	
 *	\code
 *	IsIncreasingNumber(134468) = [true]
 *	IsIncreasingNumber(249)    = [true]
 *	IsIncreasingNumber(924)    = [false]
 *	\endcode
 */
template <typename T>
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


template <typename T>
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
 *	\brief	Check if the given number \a n is decreasing or not.
 *	
 *	Working from left-to-right if no digit is exceeded by the digit to its
 *	right it is called a decreasing number; for example, 66420.
 *	
 *	\ref https://projecteuler.net/problem=112
 */
template <typename T>
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

template <typename T>
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

template <typename T> T NCR(int N, int R)
{
	R = min(R, N - R);
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
//	max(N, -N) for unsigned types.
//	
template<typename T> int GetNumberOfDigits(T N)
{
	//return N ? (int)(log10(1. * max(N, -N)) + 1) : 0;
	if (N == 0) return 0;
	if (N > 0)	return (int)(log10(1. * N) + 1);
	return (int)(log10(1. * -N) + 1);
}

// abs() doesn't work for long long that's why i have used max
template<typename T> T GCD(const T& a, const T& b)
{
	return a == 0 ? std::max<T>(b, -b) : GCD<T>(b % a, a);
}

template<> UInt64 GCD(const UInt64& a, const UInt64& b)
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
template <typename T> int GetDigitsSum(T N)
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
 *	\brief Convert the given number \a value (in decimal) to the requested base.
 *	
 *	\return String in base \a radix.
 *	
 *	\code
 *	ToRadix(N, 2)  = [11111001]
 *	ToRadix(N, 10) = [249]
 *	ToRadix(N, 16) = [F9]
 *	\endcode
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

//
// :::~numeric
//

//
// :::Strings
//

template<typename T>
T ToLower(const T& s)
{
	for (size_t i = 0; i < s.size(); ++i)
		if (isupper(s[i]))
			s[i] += 32;
	return s;
}

template<typename T>
T ToUpper(const T& s)
{
	for (size_t i = 0; i < s.size(); ++i)
		if (islower(s[i]))
			s[i] -= 32;
	return s;
}

std::string ReplaceALL(std::string s, const std::string& fnd, const std::string& rep = "") {
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
 * \brief	Gets current date time.
 *
 * \return	The current date time.
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
			sprintf_s(szDateTime, "%s %d", __TIME__, __DATE__);
		}
		else {
			szDateTime[24] = '\0';
		}
	}

	return szDateTime;
}

/**
 * \brief	Gets current date time.
 *
 * \return	The current date time.
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
			swprintf_s(szDateTime, L"%s %d", __TIME__, __DATE__);
		}
		else {
			szDateTime[24] = '\0';
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
 *	\brief Trim leading and trailing spaces (including tabs and newlines).
 *	
 *	\param[in, out]		s	C-style string.
 *	
 *	\return		String after removing leading and trailing spaces.
 */
char* Trim(char* s)
{
	if (s == NULL) return NULL;

	char* p = s + strlen(s) - 1;
	while (*p != '\0' && (*p == ' ' || *p == '\t' || *p == '\n')) --p; p[1] = '\0';
	while (*s != '\0' && (*s == ' ' || *s == '\t' || *s == '\n')) ++s;

	return s;
}


std::string Trim(const std::string& str, const std::string& whitespace = " \t")
{
	if (str.empty()) return str;
	size_t p = str.find_first_not_of(whitespace);
	if (p == std::string::npos) return "";
	size_t q = str.find_last_not_of(whitespace);
	return str.substr(p, q - p + 1);
}


std::string TrimLeft(const std::string& str, const std::string& seps = " \t")
{
	if (str.empty()) return str;
	size_t p = str.find_first_not_of(seps);
	if (p == std::string::npos) return "";
	size_t q = str.size();
	return str.substr(p, q - p + 1);
}


std::string TrimRight(const std::string& str, const std::string& seps = " \t")
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
	std::string		m_FilePath;
	std::fstream	m_fs;

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

	template <typename T> bool Read(T& t) {
		return (bool)(m_fs >> t);
	}

	template <typename T> bool Read(std::vector<std::vector<T>>& t) {
		t.clear();
		std::vector<T> vt;
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

	template <typename T> bool Read(std::vector<std::vector<T>>& vvt, const std::string& seps) {
		vvt.clear();
		std::vector<T> vt;
		while (Read(vt, seps)) {
			if (vt.empty()) return true;
			vvt.push_back(vt);
		}
		return true;
	}

	template <typename T> T Read() {
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
 *	\brief Roman Converter
 *	
 *	I = 1
 *	V = 5
 *	X = 10
 *	L = 50
 *	C = 100
 *	D = 500
 *	M = 1000
 *
 *	Rules:
 * 
 *	(1) Only I, X, and C can be used as the leading numeral in part of a subtractive pair.
 *	(2) I can only be placed before V and X.
 *	(3) X can only be placed before L and C.
 *	(4) C can only be placed before D and M.
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
#if _MSC_VER >= 1700	/* VisualStudio 2012, VC++ compiler */
		FOREACH(ch, romanNumeral) {
#else
		FOREACH(std::string, it, romanNumeral) {
			decltype(*it) ch = *it;
#endif
			ch = toupper(ch);
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
		const int	N = 13;
		long		dec[N] = { 1000, 900,  500, 400,  100,  90,  50,  40,   10,   9,    5,   4,    1  };
		std::string	num[N] = {  "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };
		std::string	numeral;

		FOR(i, (int)N) {
			while (decimal >= dec[i]) {
				decimal -= dec[i];
				numeral.append(num[i]);
			}
		}

		return numeral;
	}
};


template <typename T>
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
 *	\brief StopWatch
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
 *	\brief ScoppedTimer
 */
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
 *				   Specify width in negative, which aligns the text to left.
 *				   Default +15 (right justification)
 *				   
 * (2) Separator : Character to be placed between key & value.
 *				   Default is ':' (colon)
 */
struct PrintFormatter
{
	int		m_Width;
	_TCHAR	m_Sep;
	_TCHAR	m_Fmt[256];

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
        if (!false) {
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

LOGO_NS_END	/* LoGo namespace ends here! */

#endif /* __cplusplus ends here! */

#endif /* __LoGo_H__ */
