import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Ticket } from './entities/Ticket.entity';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: 'host.docker.internal',
      database: 'demo',
      username: 'postgres',
      password: 'teste123',
      synchronize: false,
      cache: false,
      entities: [Ticket],
    }),
    TypeOrmModule.forFeature([Ticket]),
  ],
  exports: [],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
