import cats.effect.{ExitCode, IO, IOApp}

import org.http4s._
import org.http4s.dsl.io._
import org.http4s.implicits._


package object VOSDataRouter {
    object YearQP extends QueryParamDecoderMatcher[Int]("year")
    object ProfileQP extends QueryParamDecoderMatcher[String]("profile")
    object StepQP extends QueryParamDecoderMatcher[String]("step")
    
    object OptionalGraduateQP extends OptionalQueryParamDecoderMatcher[String]("graduate")
    
    val routes = HttpRoutes.of[IO] {
        case GET -> Root / "api" / "v1" / profile / year / step :? OptionalGraduateQP(graduate) => 
            Ok(VOSDataHandlers.getOlympiadData(profile, step, year.toInt, graduate))
    }.orNotFound
}


object VOSDataHandlers {
    /*  Все endpoints для получения данных Всероссийской олимпиады школьников
    
        Все имена будут закодированы хэш функцией (для безопасности), 
        что не теряет возможность агреггировать данные по ФИО

    Получение таблицы данных
        Возвращает csv файл с данными олимпиады этого года 
        - GET api/v1/profile/step?year&graduate

        Доступны:
        - profile: {"informatics"}   // информатика
        - step: {"reg", "zakl"}      // регион и закл

        Параметры:
        - year: [2022, 2023]         // Пока только 2022 и 2023 год     
        - graduate: ["winner", "prize-winner", "participant"] // Победитель, призер или участник
    */

  def getOlympiadData(profile: String, step: String, year: Int, graduate: Optional[String]): IO[Response[IO]] = {
        /* Формат возвращаемых данных: 

        - В случае status_code == 200, ответ будет в формате csv с таблицей результатов олимпиады:
            {"message": "Success!", "data": "number, name, school, points, graduate ..."}

        - В случае, если таких данных нет, то будет получен status_code = 404
        {"message": "No such data", "data": None}

        - В случае, если данные неверные (например, year назвали "abc"), то будет получен status_code = 400
        и в message будет пояснение 
            {"message": s"Bad request, %explanation", "data": None}
        */
        IO.pure(Response[IO](Status.Ok).withEntity(responseBody))
    }
}

