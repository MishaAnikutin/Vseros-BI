import cats.effect.{IO, IOApp}
import ru.ad_olimp.backend.Server


object Main extends IOApp.Simple {
  val run = Server.run[IO]
}
