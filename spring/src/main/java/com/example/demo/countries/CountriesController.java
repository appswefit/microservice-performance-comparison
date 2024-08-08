package com.example.demo.countries;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/country")
public class CountriesController {

    @Autowired
    private CountriesService countriesService;
    
    @GetMapping("/{country}")
    public List<University> getTicketByBooking(@PathVariable("country") String country) {
        return this.countriesService.getUniversities(country);
    }     
}
