#!/usr/bin/node
exports.converter = function(base) {
    if (base < 2 || base > 36) {
    }

    return function convert(number) {
        if (number < base) {
            return number.toString(base);
        } else {
            return convert(Math.floor(number / base)) + (number % base).toString(base).toUpperCase();
        }
    };
};
