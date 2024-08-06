import { Injectable } from '@nestjs/common';
import * as universities from './data/universities.json';
import { University } from './entities/University.entity';

@Injectable()
export class AppService {
  getUniversities(country: string): University[] {
    if (country !== '') {
      return (universities as University[]).filter(
        (university) => university.country === country,
      );
    } else {
      return universities as University[];
    }
  }
}
