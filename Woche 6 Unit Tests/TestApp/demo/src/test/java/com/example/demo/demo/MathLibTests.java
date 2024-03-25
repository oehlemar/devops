package com.example.demo.demo;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

public class MathLibTests {
    @Test
    void testIsEven() {
        assertFalse(MathLib.isEven(3));
        assertTrue(MathLib.isEven(2));
    }
}
