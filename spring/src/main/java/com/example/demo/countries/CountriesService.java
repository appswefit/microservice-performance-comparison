package com.example.demo.countries;

import java.io.InputStream;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.Resource;
import org.springframework.stereotype.Service;

import com.example.demo.ResourceUtil;
import com.fasterxml.jackson.databind.ObjectMapper;

@Service
public class CountriesService {

    @Autowired
    private ResourceUtil resourceService;

    public List<University> getUniversities(String country) {
        try {
            ObjectMapper mapper = new ObjectMapper();

            Resource resource = resourceService.getResource("static/universities.json");

            InputStream inputStream = resource.getInputStream();

            List<University> universities = Arrays.asList(mapper.readValue(inputStream, University[].class));

            Predicate<University> streamsPredicate = item -> item.getCountry().equals(country);

            List<University> filtered = universities.stream()
                    .filter(streamsPredicate)
                    .collect(Collectors.toList());

            return filtered;
        } catch (Exception ex) {
            ex.printStackTrace();
        }

        return Collections.emptyList();
    }
}