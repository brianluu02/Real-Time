package com.demo.rabbitmq.controller;

import com.demo.rabbitmq.dto.Book;
import com.demo.rabbitmq.publisher.RabbitMQJsonProducer;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
public class MessageJsonController {
    public RabbitMQJsonProducer rabbitMQJsonProducer;
    public MessageJsonController(RabbitMQJsonProducer rabbitMQJsonProducer) {
        this.rabbitMQJsonProducer = rabbitMQJsonProducer;
    }
    @PostMapping("/publish")
    public ResponseEntity<String> sendJsonMessage(@RequestBody Book book) {
        rabbitMQJsonProducer.sendJsonMessage(book);
        return ResponseEntity.ok("Json message sent to RabbitMQ ...");
    }

}
