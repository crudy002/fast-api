package com.example.controller;

import com.example.model.Item;
import com.example.repository.ItemRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/items")
@CrossOrigin
public class ItemController {
    private static final Logger logger = LoggerFactory.getLogger(ItemController.class);

    @Autowired
    private ItemRepository itemRepository;

    @GetMapping
    public ResponseEntity<List<Item>> getAllItems() {
        logger.info("Fetching all items");
        List<Item> items = itemRepository.findAllItems();
        logger.info("Found {} items", items.size());
        return ResponseEntity.ok(items);
    }
}