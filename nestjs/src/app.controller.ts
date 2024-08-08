import { Controller, Get, Query } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private service: AppService) {}

  @Get('/hello')
  handleMessage(): string {
    return this.service.getHello();
  }

  @Get('/universities')
  handleUniversities(@Query('country') country: string) {
    return this.service.getUniversities(country);
  }
}
