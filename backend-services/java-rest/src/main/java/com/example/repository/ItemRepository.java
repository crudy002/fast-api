package com.example.repository;

import com.example.model.Item;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface ItemRepository extends JpaRepository<Item, Long> {
    @Query(value = "SELECT * FROM items", nativeQuery = true)
    List<Item> findAllItems();
}