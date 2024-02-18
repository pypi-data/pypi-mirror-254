"""
This code interfaces with the "primes" Rust library.
"""

# Standard imports.
from ctypes import c_char_p, c_int32, cast

# Local imports.
from .rust_utils import (
    get_local_rust_library,
    make_contact_template,
    int_to_bool
)

# Local constants.
RUST_LIB = get_local_rust_library("hosker_primes")
MAX_DIGITS = 100
BIGINT_DIGIT_LIST_C_TYPE = c_int32*MAX_DIGITS

#############
# FUNCTIONS #
#############

def make_contact():
    """ Prove that you can access this library. """
    return make_contact_template(RUST_LIB)

def is_prime_i32(n: int) -> bool:
    """ Determine whether a given 32-bit integer is prime. """
    rust_func = RUST_LIB.is_prime_i32
    rust_func.argtypes = [c_int32]
    rust_func.restype = c_int32
    rust_result = rust_func(n)
    result = int_to_bool(rust_result)
    return result

def is_prime_bigint(bigint_digit_list: list[int]) -> bool:
    """
    Determine whether an arbitrarily large number is prime, where that
    arbitrarily large number is represented by a list of "digits", and where
    each of those "digits" represents a power of 2**32, rather than of 10.
    """
    c_array = BIGINT_DIGIT_LIST_C_TYPE(*bigint_digit_list)
    rust_func = RUST_LIB.is_prime_bigint
    rust_func.argtypes = [BIGINT_DIGIT_LIST_C_TYPE]
    rust_func.restype = c_int32
    rust_result = rust_func(c_array)
    result = int_to_bool(rust_result)
    return result

def echo_big_integer(bigint_digit_list: list[int]) -> int:
    """
    EXPERIMENTAL.

    This function passes an arbitrarily large integer to Rust, and then receives
    exactly the same integer back from Rust, and returns that integer.

    Obviously, on its own this serves no earthly purpose, but it might
    demonstrate one means of passing an arbitrarily large integer from Rust
    to Python, which is not straightforward.
    """
    c_array = BIGINT_DIGIT_LIST_C_TYPE(*bigint_digit_list)
    rust_func = RUST_LIB.echo_big_integer
    rust_func.argtypes = [BIGINT_DIGIT_LIST_C_TYPE]
    rust_func.restype = c_char_p
    result_pointer = rust_func(c_array)
    result_str = cast(result_pointer, c_char_p).value.decode()
    result = int(result_str)
    return result
