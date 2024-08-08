package com.example.demo;

import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;
import org.springframework.stereotype.Service;

@Service
public class ResourceUtil {

  private final ResourceLoader resourceLoader;

  public ResourceUtil(ResourceLoader resourceLoader) {
    this.resourceLoader = resourceLoader;
  }

  public Resource getResource(String resourcePath) {
    return resourceLoader.getResource("classpath:" + resourcePath);
  }
}