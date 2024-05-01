package ru.ad_olimp.backend

import cats.effect.{ExitCode, IO, IOApp}
import org.http4s._
import org.http4s.dsl.io._
import org.http4s.implicits._

import ru.ad_olimp.backend.api.Router.{allRoutes => routes}


override def run(args: List[String]): IO[ExitCode] = {

    val builder = BlazeServerBuilder[IO](executionContext)
      .bindHttp(8080, "0.0.0.0")
      .withHttpApp(routes)

    val server = builder.resource.use(_ => IO.never).as(ExitCode.Success)

    server
  }