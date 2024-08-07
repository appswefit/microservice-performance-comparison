import { Controller, Get, Query } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private service: AppService) {}

  @Get('/hello')
  handleMessage(): string {
    return this.service.getHello();
  }

  @Get('/tickets')
  handleTickets(@Query('book_ref') bookRef: string): object {
    return this.service.getTickets(bookRef);
  }
}
