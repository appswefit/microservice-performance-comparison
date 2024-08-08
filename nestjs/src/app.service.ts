import { Injectable } from '@nestjs/common';
import * as fs from 'fs';
import path = require('path');

@Injectable()
export class AppService {
  constructor() {}

  getHello(): string {
    return 'Hello World!';
  }

  async getUniversities(country: string) {
    const jsonPath = path.join(__dirname, 'data', 'universities.json');

    const universities = await new Promise((resolve) =>
      fs.readFile(jsonPath, 'utf8', (error, data) => {
        if (error) {
          console.log(error);
          return;
        }
        const universities = JSON.parse(data).filter(
          (uni) => uni.country == country,
        );
        resolve(universities);
      }),
    );

    return universities;
  }
}
