import { Module, OnModuleInit } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { InjectRepository, TypeOrmModule } from '@nestjs/typeorm';
import { University } from './entities/University.entity';
import { Repository } from 'typeorm';
import * as universities from './data/universities.json';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'sqlite',
      database: 'db.sqlite',
      entities: [University],
      synchronize: true,
    }),
    TypeOrmModule.forFeature([University]),
  ],
  exports: [],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule implements OnModuleInit {
  constructor(
    @InjectRepository(University)
    private readonly universityRepository: Repository<University>,
  ) {}
  onModuleInit() {
    const entities = (universities as University[]).map((uni) =>
      this.universityRepository.create(uni),
    );
    this.universityRepository.save(entities);
  }
}
