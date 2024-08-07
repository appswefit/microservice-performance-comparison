import { Entity, PrimaryColumn, Column } from 'typeorm';

@Entity('tickets', { schema: 'bookings' })
export class Ticket {
  @PrimaryColumn({ type: 'character', length: 13, name: 'ticket_no' })
  ticketNo: string;

  @Column({ type: 'character', length: 6, name: 'book_ref' })
  bookRef: string;

  @Column({ type: 'varchar', length: 20, name: 'passenger_id' })
  passengerId: string;

  @Column({ type: 'text', name: 'passenger_name' })
  passengerName: string;

  @Column({ type: 'jsonb', nullable: true })
  contactData?: any;
}
