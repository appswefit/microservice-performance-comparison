package com.example.demo.countries;


import com.fasterxml.jackson.annotation.JsonProperty;

public class University {
    @JsonProperty("web_pages") 
    private String[] webPages;
    @JsonProperty("name")
    private String name;
    @JsonProperty("domains")
    private String[] domains;
    @JsonProperty("alpha_two_code") 
    private String alphaTwoCode;
    @JsonProperty("country")
    private String country;
    @JsonProperty("state-province") 
    private String stateProvince;

    public University() {
    }

    public University(String[] webPages, String name, String[] domains, String alphaTwoCode, String country, String stateProvince) {
        this.webPages = webPages;
        this.name = name;
        this.domains = domains;
        this.alphaTwoCode = alphaTwoCode;
        this.country = country;
        this.stateProvince = stateProvince;
    }

    public String getName() {
        return this.name;
    }

    public String getCountry() {
        return this.country;
    }
}