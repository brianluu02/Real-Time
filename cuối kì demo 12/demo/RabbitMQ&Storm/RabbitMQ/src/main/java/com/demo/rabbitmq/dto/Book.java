package com.demo.rabbitmq.dto;

import lombok.Data;

import java.math.BigDecimal;

@Data
public class Book {
    private Integer bookId;
    private String bookName;
    private BigDecimal price;
}
