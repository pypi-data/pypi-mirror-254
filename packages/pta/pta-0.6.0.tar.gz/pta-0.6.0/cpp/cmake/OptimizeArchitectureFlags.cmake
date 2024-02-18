macro(optimize_architecture_flags)
	if("${CMAKE_SYSTEM_PROCESSOR}" MATCHES "(x86|AMD64)")
		if(MSVC)
			add_definitions(-D__SSE__)
			set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /GL")
			if(NOT MSVC_VERSION LESS 1930)
				set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /fp:contract")
			endif()

			# Based on https://gist.github.com/UnaNancyOwen/263c243ae1e05a2f9d0e
			include(CheckCXXSourceRuns)
			set(CMAKE_REQUIRED_FLAGS)

			# Check AVX
			if(NOT MSVC_VERSION LESS 1600)
				set(CMAKE_REQUIRED_FLAGS "/arch:AVX")
			endif()
			check_cxx_source_runs("
				#include <immintrin.h>
				int main() {
					__m256 a, b, c;
					const float src[8] = { 1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f };
					float dst[8];
					a = _mm256_loadu_ps( src );
					b = _mm256_loadu_ps( src );
					c = _mm256_add_ps( a, b );
					_mm256_storeu_ps( dst, c );
					for( int i = 0; i < 8; i++ )
						if( ( src[i] + src[i] ) != dst[i] )
							return -1;
					return 0;
				}" HAS_AVX)

			# Check AVX2
			if(NOT MSVC_VERSION LESS 1800)
				set(CMAKE_REQUIRED_FLAGS "/arch:AVX2")
			endif()
	
			check_cxx_source_runs("
				#include <immintrin.h>
				int main() {
					__m256i a, b, c;
					const int src[8] = { 1, 2, 3, 4, 5, 6, 7, 8 };
					int dst[8];
					a =  _mm256_loadu_si256( (__m256i*)src );
					b =  _mm256_loadu_si256( (__m256i*)src );
					c = _mm256_add_epi32( a, b );
					_mm256_storeu_si256( (__m256i*)dst, c );
					for( int i = 0; i < 8; i++ )
						if( ( src[i] + src[i] ) != dst[i] )
							return -1;
					return 0;
				}" HAS_AVX2)

			# Set flags
			if(HAS_AVX2 AND NOT MSVC_VERSION LESS 1800)
				set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /arch:AVX2")
			elseif(HAS_AVX  AND NOT MSVC_VERSION LESS 1600)
				set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /arch:AVX")
			endif()
		else()
			set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=native -ffp-contract=fast")	
		endif()
	else()
		message("Build flags will not be optimized since the CPU is not x86 or AMD64")
	endif()
endmacro(optimize_architecture_flags)