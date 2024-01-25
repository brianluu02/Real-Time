//package com.demo.rabbitmq.consumer;
//
//import com.demo.rabbitmq.dto.Book;
//import org.slf4j.Logger;
//import org.slf4j.LoggerFactory;
//import org.springframework.amqp.rabbit.annotation.RabbitListener;
//import org.springframework.stereotype.Service;
//
//@Service
//public class RabbitMQJsonConsumer {
//    private static final Logger LOGGER = LoggerFactory.getLogger(RabbitMQJsonConsumer.class);
//
//    @RabbitListener(queues = {"${rabbitmq.queue.json.name}"})
//    public void consumeJsonMessage(Book book) {
//        LOGGER.info(String.format("Received Json message -> %s", book.toString()));
//    }
//}
