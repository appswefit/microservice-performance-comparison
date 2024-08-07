import { InjectRepository } from '@nestjs/typeorm';
import { Injectable } from '@nestjs/common';
import { Repository } from 'typeorm';
import { Ticket } from './entities/Ticket.entity';
const _delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
function _getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

@Injectable()
export class AppService {
  constructor(
    @InjectRepository(Ticket)
    private readonly ticketRepository: Repository<Ticket>,
  ) {}

  getHello(): string {
    return 'Hello World!';
  }

  async getTickets(bookRef: string) {
    const tickets = await this.ticketRepository.find({
      select: { ticketNo: true, passengerId: true, passengerName: true },
      take: 1000,
    });
    return tickets.filter((t) => t.bookRef === bookRef);
  }
}
