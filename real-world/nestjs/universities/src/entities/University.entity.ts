import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';

@Entity()
export class University {
  @PrimaryGeneratedColumn()
  id: number;

  @Column('simple-array', { nullable: true, array: true })
  web_pages: string[];

  @Column()
  name: string;

  @Column('simple-array', { nullable: true, array: true })
  domains: string[];

  @Column()
  alpha_two_code: string;

  @Column()
  country: string;

  @Column({ nullable: true })
  'state-province'?: string;
}
