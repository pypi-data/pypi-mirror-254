/// This library defines some utility functions for working with primes.

// Standard imports.
use std::ffi::CString;

// Non-standard imports.
use libc::c_char;
use num_bigint::{BigInt, Sign};
use num_integer::Integer;
use num_iter;
use primes;

// Local constants.
const MAX_DIGITS: usize = 100;
const STANDARD_RADIX: u32 = 10;
const TRUE_INT: i32 = 1;
const FALSE_INT: i32 = 0;

/***************************
 ** FOR INTERNAL USE ONLY **
 **************************/

/// Determine whether an arbitrarily large integer is prime.
fn _is_prime_bigint(potential_prime: BigInt) -> bool {
println!("Received: {:?}", potential_prime);
    if potential_prime == BigInt::from(2) {
        return true;
    }
    if potential_prime.is_even() {
        return false;
    }

    let max_potential_divisor = potential_prime.sqrt();

    for potential_divisor in num_iter::range_inclusive(
        BigInt::from(3), max_potential_divisor
    ) {
        if potential_prime.is_multiple_of(&potential_divisor) {
            return false;
        }
    }

    return true;
}

// Middleman functions for the rest of this section...

/// Receive a big integer from outside Rust.
unsafe fn import_bigint(digit_list: PortableDigitList) -> BigInt {
    let digits = Vec::from(*digit_list.array);
    let result = BigInt::new(Sign::Plus, digits);

    return result;
}

/// Convert a big integer into an exportable form outside Rust.
fn export_bigint(n: BigInt) -> *mut c_char {
    let result_str = n.to_str_radix(STANDARD_RADIX);
    let result = CString::new(result_str).unwrap().into_raw();

    return result;
}

/// Convert a boolean into an integer representation of the same.
fn bool_to_int(boolean: bool) -> i32 {
    if boolean {
        return TRUE_INT;
    }

    return FALSE_INT;
}

/****************
 ** FOR EXPORT **
 ***************/

/// A portable representation of a large integer.
#[repr(C)]
pub struct PortableDigitList {
    array: *const [u32; MAX_DIGITS]
}

/// Reassure an external user that they can indeed access this library.
#[no_mangle]
pub extern fn make_contact(int: i32) {
    println!("Congratulations! You have made contact with the PRIMES library.");
    println!("This is the integer you gave me: {}", int);
}

/// Receive a big integer from outside Rust, and send it back.
#[no_mangle]
pub unsafe extern fn echo_big_integer(
    digit_list: PortableDigitList
) -> *mut c_char {
    let big_integer = import_bigint(digit_list);

    println!("Received big integer: {:?}. Sending it back...", big_integer);

    return export_bigint(big_integer);
}

/// Prevent a memory leak from sending a reference to a C string outside Rust.
#[no_mangle]
pub unsafe extern fn free_string(pointer: *mut c_char) {
    let _ = CString::from_raw(pointer);
}

/// A wrapper for the similarly-named function above.
#[no_mangle]
pub extern fn is_prime_i32(n: i32) -> i32 {
    return bool_to_int(primes::is_prime(n.try_into().unwrap()));
}

/// A wrapper for the similarly-named function above.
#[no_mangle]
pub unsafe extern fn is_prime_bigint(digit_list: PortableDigitList) -> i32 {
    let digits = Vec::from(*digit_list.array);
println!("{:?}", digits);
    let big_integer = BigInt::new(Sign::Plus, digits);

    return bool_to_int(_is_prime_bigint(big_integer));
}
