FROM maven:3.9.6-eclipse-temurin-22-alpine AS builder

COPY pom.xml .
COPY src ./src

RUN mvn clean package -DskipTests



FROM openjdk:22-jdk
VOLUME /tmp
COPY --from=BUILDER target/demo-0.0.1-SNAPSHOT.jar .
CMD ["java", "-jar", "demo-0.0.1-SNAPSHOT.jar"]
