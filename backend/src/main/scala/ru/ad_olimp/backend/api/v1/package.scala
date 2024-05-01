import cats.effect.{ExitCode, IO, IOApp}

import org.http4s._
import org.http4s.dsl.io._
import org.http4s.implicits._

import VOSDataHandlers.{VOSDataRouter}


package object Router {
  val vosDataRoutes: HttpRoutes[IO] = VOSDataRouter.routes

  val allRoutes: HttpRoutes[IO] = vosDataRoutes <+> userRoutes
}


