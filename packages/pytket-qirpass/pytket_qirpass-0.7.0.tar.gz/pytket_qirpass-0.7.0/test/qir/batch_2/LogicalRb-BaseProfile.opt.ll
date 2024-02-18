; ModuleID = 'qir/LogicalRb-BaseProfile.ll'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

define void @Microsoft__Quantum__Samples__RunMain__Interop() local_unnamed_addr #0 {
entry:
  tail call fastcc void @Microsoft__Quantum__Samples__RunMain__body.1()
  ret void
}

declare void @__quantum__qis__reset__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*) local_unnamed_addr

declare void @__quantum__qis__h__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__x__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__z__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__y__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__cz__body(%Qubit*, %Qubit*) local_unnamed_addr

declare void @__quantum__qis__s__adj(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__s__body(%Qubit*) local_unnamed_addr

declare i64 @__quantum__qis__drawrandomint__body(i64, i64) local_unnamed_addr

define internal fastcc void @Microsoft__Quantum__Samples__RunMain__body.1() unnamed_addr {
entry:
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__y__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %body__1

body__1:                                          ; preds = %Microsoft__Quantum__Samples__Recover__body.8.exit, %entry
  %0 = phi i64 [ 1, %entry ], [ %133, %Microsoft__Quantum__Samples__Recover__body.8.exit ]
  %acc.032 = phi i64 [ 0, %entry ], [ %66, %Microsoft__Quantum__Samples__Recover__body.8.exit ]
  %1 = tail call i64 @__quantum__qis__drawrandomint__body(i64 0, i64 23)
  %2 = lshr i64 %1, 4
  %3 = and i64 %2, 3
  %4 = lshr i64 %1, 3
  %5 = and i64 %4, 1
  %6 = lshr i64 %acc.032, 6
  %7 = and i64 %6, 3
  %8 = icmp eq i64 %3, 0
  %9 = icmp eq i64 %5, 0
  %10 = or i64 %3, %5
  %11 = icmp eq i64 %10, 0
  %12 = icmp eq i64 %7, 0
  %13 = or i64 %10, %7
  %14 = icmp eq i64 %13, 0
  br i1 %14, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test1__1.i.i

test1__1.i.i:                                     ; preds = %body__1
  %15 = icmp eq i64 %7, 1
  %16 = and i1 %15, %11
  br i1 %16, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test2__1.i.i

test2__1.i.i:                                     ; preds = %test1__1.i.i
  %17 = icmp eq i64 %7, 2
  %18 = and i1 %17, %11
  br i1 %18, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test3__1.i.i

test3__1.i.i:                                     ; preds = %test2__1.i.i
  %19 = icmp ne i64 %5, 0
  %spec.select3.i.i = and i1 %8, %19
  %20 = and i1 %12, %spec.select3.i.i
  br i1 %20, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test4__1.i.i

test4__1.i.i:                                     ; preds = %test3__1.i.i
  %21 = and i1 %15, %spec.select3.i.i
  br i1 %21, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test5__1.i.i

test5__1.i.i:                                     ; preds = %test4__1.i.i
  %22 = and i1 %17, %spec.select3.i.i
  br i1 %22, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test6__1.i.i

test6__1.i.i:                                     ; preds = %test5__1.i.i
  %23 = icmp eq i64 %3, 1
  %spec.select6.i.i = and i1 %23, %9
  %24 = and i1 %12, %spec.select6.i.i
  br i1 %24, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test7__1.i.i

test7__1.i.i:                                     ; preds = %test6__1.i.i
  %25 = and i1 %15, %spec.select6.i.i
  br i1 %25, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test8__1.i.i

test8__1.i.i:                                     ; preds = %test7__1.i.i
  %26 = and i1 %17, %spec.select6.i.i
  br i1 %26, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test9__1.i.i

test9__1.i.i:                                     ; preds = %test8__1.i.i
  %spec.select9.i.i = and i1 %23, %19
  %27 = and i1 %12, %spec.select9.i.i
  br i1 %27, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test10__1.i.i

test10__1.i.i:                                    ; preds = %test9__1.i.i
  %28 = and i1 %15, %spec.select9.i.i
  br i1 %28, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test11__1.i.i

test11__1.i.i:                                    ; preds = %test10__1.i.i
  %29 = and i1 %17, %spec.select9.i.i
  br i1 %29, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test12__1.i.i

test12__1.i.i:                                    ; preds = %test11__1.i.i
  %30 = icmp eq i64 %3, 2
  %spec.select12.i.i = and i1 %30, %9
  %31 = and i1 %12, %spec.select12.i.i
  br i1 %31, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test13__1.i.i

test13__1.i.i:                                    ; preds = %test12__1.i.i
  %32 = and i1 %15, %spec.select12.i.i
  br i1 %32, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test14__1.i.i

test14__1.i.i:                                    ; preds = %test13__1.i.i
  %33 = and i1 %17, %spec.select12.i.i
  br i1 %33, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test15__1.i.i

test15__1.i.i:                                    ; preds = %test14__1.i.i
  %spec.select15.i.i = and i1 %30, %19
  %34 = and i1 %12, %spec.select15.i.i
  br i1 %34, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test16__1.i.i

test16__1.i.i:                                    ; preds = %test15__1.i.i
  %35 = and i1 %15, %spec.select15.i.i
  br i1 %35, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test17__1.i.i

test17__1.i.i:                                    ; preds = %test16__1.i.i
  %36 = and i1 %17, %spec.select15.i.i
  br i1 %36, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test18__1.i.i

test18__1.i.i:                                    ; preds = %test17__1.i.i
  %37 = icmp eq i64 %3, 3
  %spec.select18.i.i = and i1 %37, %9
  %38 = and i1 %12, %spec.select18.i.i
  br i1 %38, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test19__1.i.i

test19__1.i.i:                                    ; preds = %test18__1.i.i
  %39 = and i1 %15, %spec.select18.i.i
  br i1 %39, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test20__1.i.i

test20__1.i.i:                                    ; preds = %test19__1.i.i
  %40 = and i1 %17, %spec.select18.i.i
  br i1 %40, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test21__1.i.i

test21__1.i.i:                                    ; preds = %test20__1.i.i
  %spec.select21.i.i = and i1 %37, %19
  %41 = and i1 %12, %spec.select21.i.i
  br i1 %41, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test22__1.i.i

test22__1.i.i:                                    ; preds = %test21__1.i.i
  %42 = and i1 %15, %spec.select21.i.i
  br i1 %42, label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i, label %test23__1.i.i

test23__1.i.i:                                    ; preds = %test22__1.i.i
  %43 = and i1 %17, %spec.select21.i.i
  %..i.i = select i1 %43, i64 120, i64 0
  br label %Microsoft__Quantum__Samples__XSECommutation__body.exit.i

Microsoft__Quantum__Samples__XSECommutation__body.exit.i: ; preds = %test23__1.i.i, %test22__1.i.i, %test21__1.i.i, %test20__1.i.i, %test19__1.i.i, %test18__1.i.i, %test17__1.i.i, %test16__1.i.i, %test15__1.i.i, %test14__1.i.i, %test13__1.i.i, %test12__1.i.i, %test11__1.i.i, %test10__1.i.i, %test9__1.i.i, %test8__1.i.i, %test7__1.i.i, %test6__1.i.i, %test5__1.i.i, %test4__1.i.i, %test3__1.i.i, %test2__1.i.i, %test1__1.i.i, %body__1
  %merge.i.i = phi i64 [ 0, %body__1 ], [ 64, %test1__1.i.i ], [ 128, %test2__1.i.i ], [ 8, %test3__1.i.i ], [ 96, %test4__1.i.i ], [ 174, %test5__1.i.i ], [ 16, %test6__1.i.i ], [ 182, %test7__1.i.i ], [ 90, %test8__1.i.i ], [ 24, %test9__1.i.i ], [ 150, %test10__1.i.i ], [ 116, %test11__1.i.i ], [ 32, %test12__1.i.i ], [ 110, %test13__1.i.i ], [ 136, %test14__1.i.i ], [ 40, %test15__1.i.i ], [ 74, %test16__1.i.i ], [ 162, %test17__1.i.i ], [ 48, %test18__1.i.i ], [ 156, %test19__1.i.i ], [ 82, %test20__1.i.i ], [ 56, %test21__1.i.i ], [ 184, %test22__1.i.i ], [ %..i.i, %test23__1.i.i ]
  %44 = lshr i64 %merge.i.i, 3
  %45 = and i64 %44, 1
  %46 = lshr i64 %acc.032, 4
  %47 = and i64 %46, 3
  %48 = icmp eq i64 %45, 0
  %49 = icmp eq i64 %47, 0
  %50 = or i64 %45, %47
  %51 = icmp eq i64 %50, 0
  br i1 %51, label %Microsoft__Quantum__Samples__Times1C__body.exit, label %test1__1.i2.i

test1__1.i2.i:                                    ; preds = %Microsoft__Quantum__Samples__XSECommutation__body.exit.i
  %52 = icmp eq i64 %47, 1
  %spec.select1.i.i = and i1 %52, %48
  br i1 %spec.select1.i.i, label %Microsoft__Quantum__Samples__Times1C__body.exit, label %test2__1.i3.i

test2__1.i3.i:                                    ; preds = %test1__1.i2.i
  %53 = icmp eq i64 %47, 2
  %spec.select2.i.i = and i1 %53, %48
  br i1 %spec.select2.i.i, label %Microsoft__Quantum__Samples__Times1C__body.exit, label %test3__1.i5.i

test3__1.i5.i:                                    ; preds = %test2__1.i3.i
  %54 = icmp eq i64 %47, 3
  %spec.select3.i4.i = and i1 %54, %48
  br i1 %spec.select3.i4.i, label %Microsoft__Quantum__Samples__Times1C__body.exit, label %test4__1.i6.i

test4__1.i6.i:                                    ; preds = %test3__1.i5.i
  %55 = icmp ne i64 %45, 0
  %spec.select4.i.i = and i1 %49, %55
  br i1 %spec.select4.i.i, label %Microsoft__Quantum__Samples__Times1C__body.exit, label %test5__1.i7.i

test5__1.i7.i:                                    ; preds = %test4__1.i6.i
  %spec.select5.i.i = and i1 %52, %55
  br i1 %spec.select5.i.i, label %Microsoft__Quantum__Samples__Times1C__body.exit, label %test6__1.i9.i

test6__1.i9.i:                                    ; preds = %test5__1.i7.i
  %spec.select6.i8.i = and i1 %53, %55
  br i1 %spec.select6.i8.i, label %Microsoft__Quantum__Samples__Times1C__body.exit, label %test7__1.i11.i

test7__1.i11.i:                                   ; preds = %test6__1.i9.i
  %spec.select7.i.i = and i1 %54, %55
  %..i10.i = select i1 %spec.select7.i.i, i64 30, i64 0
  br label %Microsoft__Quantum__Samples__Times1C__body.exit

Microsoft__Quantum__Samples__Times1C__body.exit:  ; preds = %test7__1.i11.i, %test6__1.i9.i, %test5__1.i7.i, %test4__1.i6.i, %test3__1.i5.i, %test2__1.i3.i, %test1__1.i2.i, %Microsoft__Quantum__Samples__XSECommutation__body.exit.i
  %merge.i1.i = phi i64 [ 0, %Microsoft__Quantum__Samples__XSECommutation__body.exit.i ], [ 16, %test1__1.i2.i ], [ 32, %test2__1.i3.i ], [ 48, %test3__1.i5.i ], [ 8, %test4__1.i6.i ], [ 58, %test5__1.i7.i ], [ 44, %test6__1.i9.i ], [ %..i10.i, %test7__1.i11.i ]
  %56 = and i64 %1, 192
  %57 = and i64 %merge.i.i, 48
  %58 = and i64 %merge.i1.i, 8
  %59 = add nuw nsw i64 %merge.i.i, %56
  %60 = and i64 %59, 192
  %61 = add nuw nsw i64 %merge.i1.i, %57
  %62 = and i64 %61, 48
  %63 = or i64 %62, %60
  %right.mask.i = and i64 %acc.032, 8
  %64 = add nuw nsw i64 %58, %right.mask.i
  %65 = and i64 %64, 8
  %66 = or i64 %63, %65
  %67 = and i64 %1, 8
  %.not.i = icmp eq i64 %67, 0
  br i1 %.not.i, label %continue__1.i, label %then0__1.i

then0__1.i:                                       ; preds = %Microsoft__Quantum__Samples__Times1C__body.exit
  tail call void @__quantum__qis__x__body(%Qubit* null)
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %continue__1.i

continue__1.i:                                    ; preds = %then0__1.i, %Microsoft__Quantum__Samples__Times1C__body.exit
  %trunc.i = trunc i64 %2 to i2
  switch i2 %trunc.i, label %continue__2.i [
    i2 1, label %then0__2.i
    i2 -2, label %then1__1.i
    i2 -1, label %then2__1.i
  ]

then0__2.i:                                       ; preds = %continue__1.i
  tail call void @__quantum__qis__s__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__s__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__s__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__s__body(%Qubit* null)
  br label %continue__2.i

then1__1.i:                                       ; preds = %continue__1.i
  tail call void @__quantum__qis__z__body(%Qubit* null)
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %continue__2.i

then2__1.i:                                       ; preds = %continue__1.i
  tail call void @__quantum__qis__s__adj(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %continue__2.i

continue__2.i:                                    ; preds = %then2__1.i, %then1__1.i, %then0__2.i, %continue__1.i
  %68 = lshr i64 %1, 6
  %trunc1.i = trunc i64 %68 to i2
  switch i2 %trunc1.i, label %Microsoft__Quantum__Samples__ApplyLogicalClifford__body.2.exit [
    i2 1, label %continue__3.sink.split.i
    i2 -2, label %then1__2.i
  ]

then1__2.i:                                       ; preds = %continue__2.i
  tail call void @__quantum__qis__s__adj(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %continue__3.sink.split.i

continue__3.sink.split.i:                         ; preds = %then1__2.i, %continue__2.i
  tail call void @__quantum__qis__s__adj(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %Microsoft__Quantum__Samples__ApplyLogicalClifford__body.2.exit

Microsoft__Quantum__Samples__ApplyLogicalClifford__body.2.exit: ; preds = %continue__3.sink.split.i, %continue__2.i
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Result* null)
  tail call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Result* nonnull inttoptr (i64 1 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Result* nonnull inttoptr (i64 2 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__cz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Result* nonnull inttoptr (i64 3 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  %69 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %69, label %test1__1.i, label %condContinue__1.i

condContinue__1.i:                                ; preds = %Microsoft__Quantum__Samples__ApplyLogicalClifford__body.2.exit
  %70 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %70, label %test1__1.i, label %condContinue__2.i

condContinue__2.i:                                ; preds = %condContinue__1.i
  %71 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %71, label %test1__1.i, label %condContinue__3.i

condContinue__3.i:                                ; preds = %condContinue__2.i
  %72 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %72, label %test1__1.i, label %Microsoft__Quantum__Samples__Recover__body.8.exit

test1__1.i:                                       ; preds = %condContinue__3.i, %condContinue__2.i, %condContinue__1.i, %Microsoft__Quantum__Samples__ApplyLogicalClifford__body.2.exit
  %73 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %73, label %test2__1.i, label %condContinue__4.i

condContinue__4.i:                                ; preds = %test1__1.i
  %74 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %74, label %test2__1.i, label %condContinue__5.i

condContinue__5.i:                                ; preds = %condContinue__4.i
  %75 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %75, label %test2__1.i, label %condTrue__6.i

condTrue__6.i:                                    ; preds = %condContinue__5.i
  %76 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %76, label %then1__1.i1, label %test2__1.i

then1__1.i1:                                      ; preds = %condTrue__6.i
  tail call void @__quantum__qis__x__body(%Qubit* null)
  br label %Microsoft__Quantum__Samples__Recover__body.8.exit

test2__1.i:                                       ; preds = %condTrue__6.i, %condContinue__5.i, %condContinue__4.i, %test1__1.i
  %77 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %77, label %test3__1.i, label %condContinue__7.i

condContinue__7.i:                                ; preds = %test2__1.i
  %78 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %78, label %test3__1.i, label %condTrue__8.i

condTrue__8.i:                                    ; preds = %condContinue__7.i
  %79 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %79, label %condContinue__9.i, label %test3__1.i

condContinue__9.i:                                ; preds = %condTrue__8.i
  %80 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %80, label %test3__1.i, label %then2__1.i2

then2__1.i2:                                      ; preds = %condContinue__9.i
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.8.exit

test3__1.i:                                       ; preds = %condContinue__9.i, %condTrue__8.i, %condContinue__7.i, %test2__1.i
  %81 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %81, label %test4__1.i, label %condContinue__10.i

condContinue__10.i:                               ; preds = %test3__1.i
  %82 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %82, label %test4__1.i, label %condTrue__11.i

condTrue__11.i:                                   ; preds = %condContinue__10.i
  %83 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %83, label %condContinue__12.i, label %test4__1.i

condContinue__12.i:                               ; preds = %condTrue__11.i
  %84 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %84, label %then3__1.i, label %test4__1.i

then3__1.i:                                       ; preds = %condContinue__12.i
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.8.exit

test4__1.i:                                       ; preds = %condContinue__12.i, %condTrue__11.i, %condContinue__10.i, %test3__1.i
  %85 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %85, label %test5__1.i, label %condContinue__13.i

condContinue__13.i:                               ; preds = %test4__1.i
  %86 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %86, label %condContinue__14.i, label %test5__1.i

condContinue__14.i:                               ; preds = %condContinue__13.i
  %87 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %87, label %test5__1.i, label %condContinue__15.i

condContinue__15.i:                               ; preds = %condContinue__14.i
  %88 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %88, label %test5__1.i, label %then4__1.i

then4__1.i:                                       ; preds = %condContinue__15.i
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.8.exit

test5__1.i:                                       ; preds = %condContinue__15.i, %condContinue__14.i, %condContinue__13.i, %test4__1.i
  %89 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %89, label %test6__1.i, label %condContinue__16.i

condContinue__16.i:                               ; preds = %test5__1.i
  %90 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %90, label %condContinue__17.i, label %test6__1.i

condContinue__17.i:                               ; preds = %condContinue__16.i
  %91 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %91, label %test6__1.i, label %condContinue__18.i

condContinue__18.i:                               ; preds = %condContinue__17.i
  %92 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %92, label %then5__1.i, label %test6__1.i

then5__1.i:                                       ; preds = %condContinue__18.i
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.8.exit

test6__1.i:                                       ; preds = %condContinue__18.i, %condContinue__17.i, %condContinue__16.i, %test5__1.i
  %93 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %93, label %test7__1.i, label %condContinue__19.i

condContinue__19.i:                               ; preds = %test6__1.i
  %94 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %94, label %condContinue__20.i, label %test7__1.i

condContinue__20.i:                               ; preds = %condContinue__19.i
  %95 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %95, label %condContinue__21.i, label %test7__1.i

condContinue__21.i:                               ; preds = %condContinue__20.i
  %96 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %96, label %test7__1.i, label %then6__1.i

then6__1.i:                                       ; preds = %condContinue__21.i
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.8.exit

test7__1.i:                                       ; preds = %condContinue__21.i, %condContinue__20.i, %condContinue__19.i, %test6__1.i
  %97 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %97, label %test8__1.i, label %condContinue__22.i

condContinue__22.i:                               ; preds = %test7__1.i
  %98 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %98, label %condContinue__23.i, label %test8__1.i

condContinue__23.i:                               ; preds = %condContinue__22.i
  %99 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %99, label %condContinue__24.i, label %test8__1.i

condContinue__24.i:                               ; preds = %condContinue__23.i
  %100 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %100, label %then7__1.i, label %test8__1.i

then7__1.i:                                       ; preds = %condContinue__24.i
  tail call void @__quantum__qis__y__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.8.exit

test8__1.i:                                       ; preds = %condContinue__24.i, %condContinue__23.i, %condContinue__22.i, %test7__1.i
  %101 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %101, label %condContinue__25.i, label %test9__1.i

condContinue__25.i:                               ; preds = %test8__1.i
  %102 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %102, label %test9__1.i, label %condContinue__26.i

condContinue__26.i:                               ; preds = %condContinue__25.i
  %103 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %103, label %test9__1.i, label %condContinue__27.i

condContinue__27.i:                               ; preds = %condContinue__26.i
  %104 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %104, label %test9__1.i, label %then8__1.i

then8__1.i:                                       ; preds = %condContinue__27.i
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.8.exit

test9__1.i:                                       ; preds = %condContinue__27.i, %condContinue__26.i, %condContinue__25.i, %test8__1.i
  %105 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %105, label %condContinue__28.i, label %test10__1.i

condContinue__28.i:                               ; preds = %test9__1.i
  %106 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %106, label %test10__1.i, label %condContinue__29.i

condContinue__29.i:                               ; preds = %condContinue__28.i
  %107 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %107, label %test10__1.i, label %condContinue__30.i

condContinue__30.i:                               ; preds = %condContinue__29.i
  %108 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %108, label %then9__1.i, label %test10__1.i

then9__1.i:                                       ; preds = %condContinue__30.i
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.8.exit

test10__1.i:                                      ; preds = %condContinue__30.i, %condContinue__29.i, %condContinue__28.i, %test9__1.i
  %109 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %109, label %condContinue__31.i, label %test11__1.i

condContinue__31.i:                               ; preds = %test10__1.i
  %110 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %110, label %test11__1.i, label %condContinue__32.i

condContinue__32.i:                               ; preds = %condContinue__31.i
  %111 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %111, label %condContinue__33.i, label %test11__1.i

condContinue__33.i:                               ; preds = %condContinue__32.i
  %112 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %112, label %test11__1.i, label %then10__1.i

then10__1.i:                                      ; preds = %condContinue__33.i
  tail call void @__quantum__qis__z__body(%Qubit* null)
  br label %Microsoft__Quantum__Samples__Recover__body.8.exit

test11__1.i:                                      ; preds = %condContinue__33.i, %condContinue__32.i, %condContinue__31.i, %test10__1.i
  %113 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %113, label %condContinue__34.i, label %test12__1.i

condContinue__34.i:                               ; preds = %test11__1.i
  %114 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %114, label %test12__1.i, label %condContinue__35.i

condContinue__35.i:                               ; preds = %condContinue__34.i
  %115 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %115, label %condContinue__36.i, label %test12__1.i

condContinue__36.i:                               ; preds = %condContinue__35.i
  %116 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %116, label %then11__1.i, label %test12__1.i

then11__1.i:                                      ; preds = %condContinue__36.i
  tail call void @__quantum__qis__y__body(%Qubit* null)
  br label %Microsoft__Quantum__Samples__Recover__body.8.exit

test12__1.i:                                      ; preds = %condContinue__36.i, %condContinue__35.i, %condContinue__34.i, %test11__1.i
  %117 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %117, label %condContinue__37.i, label %test13__1.i

condContinue__37.i:                               ; preds = %test12__1.i
  %118 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %118, label %condContinue__38.i, label %test13__1.i

condContinue__38.i:                               ; preds = %condContinue__37.i
  %119 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %119, label %test13__1.i, label %condContinue__39.i

condContinue__39.i:                               ; preds = %condContinue__38.i
  %120 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %120, label %test13__1.i, label %then12__1.i

then12__1.i:                                      ; preds = %condContinue__39.i
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.8.exit

test13__1.i:                                      ; preds = %condContinue__39.i, %condContinue__38.i, %condContinue__37.i, %test12__1.i
  %121 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %121, label %condContinue__40.i, label %test14__1.i

condContinue__40.i:                               ; preds = %test13__1.i
  %122 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %122, label %condContinue__41.i, label %test14__1.i

condContinue__41.i:                               ; preds = %condContinue__40.i
  %123 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %123, label %test14__1.i, label %condContinue__42.i

condContinue__42.i:                               ; preds = %condContinue__41.i
  %124 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %124, label %then13__1.i, label %test14__1.i

then13__1.i:                                      ; preds = %condContinue__42.i
  tail call void @__quantum__qis__y__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.8.exit

test14__1.i:                                      ; preds = %condContinue__42.i, %condContinue__41.i, %condContinue__40.i, %test13__1.i
  %125 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %125, label %condContinue__43.i, label %test15__1.i

condContinue__43.i:                               ; preds = %test14__1.i
  %126 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %126, label %condContinue__44.i, label %test15__1.i

condContinue__44.i:                               ; preds = %condContinue__43.i
  %127 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %127, label %condContinue__45.i, label %test15__1.i

condContinue__45.i:                               ; preds = %condContinue__44.i
  %128 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %128, label %test15__1.i, label %then14__1.i

then14__1.i:                                      ; preds = %condContinue__45.i
  tail call void @__quantum__qis__y__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.8.exit

test15__1.i:                                      ; preds = %condContinue__45.i, %condContinue__44.i, %condContinue__43.i, %test14__1.i
  %129 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %129, label %condContinue__46.i, label %Microsoft__Quantum__Samples__Recover__body.8.exit

condContinue__46.i:                               ; preds = %test15__1.i
  %130 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %130, label %condContinue__47.i, label %Microsoft__Quantum__Samples__Recover__body.8.exit

condContinue__47.i:                               ; preds = %condContinue__46.i
  %131 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %131, label %condContinue__48.i, label %Microsoft__Quantum__Samples__Recover__body.8.exit

condContinue__48.i:                               ; preds = %condContinue__47.i
  %132 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %132, label %then15__1.i, label %Microsoft__Quantum__Samples__Recover__body.8.exit

then15__1.i:                                      ; preds = %condContinue__48.i
  tail call void @__quantum__qis__y__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.8.exit

Microsoft__Quantum__Samples__Recover__body.8.exit: ; preds = %then15__1.i, %condContinue__48.i, %condContinue__47.i, %condContinue__46.i, %test15__1.i, %then14__1.i, %then13__1.i, %then12__1.i, %then11__1.i, %then10__1.i, %then9__1.i, %then8__1.i, %then7__1.i, %then6__1.i, %then5__1.i, %then4__1.i, %then3__1.i, %then2__1.i2, %then1__1.i1, %condContinue__3.i
  %133 = add nuw nsw i64 %0, 1
  %134 = icmp ult i64 %0, 30
  br i1 %134, label %body__1, label %exit__1

exit__1:                                          ; preds = %Microsoft__Quantum__Samples__Recover__body.8.exit
  %135 = lshr exact i64 %60, 6
  %136 = lshr exact i64 %62, 4
  %137 = lshr exact i64 %64, 3
  %138 = and i64 %137, 1
  %139 = icmp eq i64 %60, 0
  %140 = icmp eq i64 %62, 0
  %141 = or i64 %136, %135
  %142 = icmp eq i64 %138, 0
  %143 = or i64 %141, %138
  %144 = icmp eq i64 %143, 0
  br i1 %144, label %Microsoft__Quantum__Samples__ApplyLogicalClifford__body.9.exit, label %test1__1.i.i2

test1__1.i.i2:                                    ; preds = %exit__1
  %145 = icmp eq i64 %141, 0
  %146 = icmp ne i64 %138, 0
  %147 = and i1 %146, %145
  br i1 %147, label %then0__1.i5, label %test2__1.i.i4

test2__1.i.i4:                                    ; preds = %test1__1.i.i2
  %148 = icmp eq i64 %62, 16
  %spec.select2.i.i3 = and i1 %139, %148
  %149 = and i1 %spec.select2.i.i3, %142
  br i1 %149, label %then2__1.i10, label %test3__1.i.i5

test3__1.i.i5:                                    ; preds = %test2__1.i.i4
  %150 = and i1 %spec.select2.i.i3, %146
  br i1 %150, label %then0__1.i5, label %test4__1.i.i7

test4__1.i.i7:                                    ; preds = %test3__1.i.i5
  %151 = icmp eq i64 %62, 32
  %spec.select4.i.i6 = and i1 %139, %151
  %152 = and i1 %spec.select4.i.i6, %142
  br i1 %152, label %then1__1.i9, label %test5__1.i.i8

test5__1.i.i8:                                    ; preds = %test4__1.i.i7
  %153 = and i1 %spec.select4.i.i6, %146
  br i1 %153, label %then0__1.i5, label %test6__1.i.i10

test6__1.i.i10:                                   ; preds = %test5__1.i.i8
  %154 = icmp eq i64 %62, 48
  %spec.select6.i.i9 = and i1 %139, %154
  %155 = and i1 %spec.select6.i.i9, %142
  br i1 %155, label %then0__2.i8, label %test7__1.i.i11

test7__1.i.i11:                                   ; preds = %test6__1.i.i10
  %156 = and i1 %spec.select6.i.i9, %146
  br i1 %156, label %then0__1.i5, label %test8__1.i.i12

test8__1.i.i12:                                   ; preds = %test7__1.i.i11
  %157 = icmp eq i64 %60, 64
  %spec.select8.i.i = and i1 %157, %140
  %158 = and i1 %spec.select8.i.i, %142
  br i1 %158, label %then1__2.i13, label %test9__1.i.i13

test9__1.i.i13:                                   ; preds = %test8__1.i.i12
  %159 = and i1 %spec.select8.i.i, %146
  br i1 %159, label %then0__1.i5, label %test10__1.i.i14

test10__1.i.i14:                                  ; preds = %test9__1.i.i13
  %spec.select10.i.i = and i1 %157, %148
  %160 = and i1 %spec.select10.i.i, %142
  br i1 %160, label %then0__2.i8, label %test11__1.i.i15

test11__1.i.i15:                                  ; preds = %test10__1.i.i14
  %161 = and i1 %spec.select10.i.i, %146
  br i1 %161, label %then2__1.i10, label %test12__1.i.i17

test12__1.i.i17:                                  ; preds = %test11__1.i.i15
  %spec.select12.i.i16 = and i1 %157, %151
  %162 = and i1 %spec.select12.i.i16, %142
  br i1 %162, label %then0__1.i5, label %test13__1.i.i18

test13__1.i.i18:                                  ; preds = %test12__1.i.i17
  %163 = and i1 %spec.select12.i.i16, %146
  br i1 %163, label %then1__1.i9, label %test14__1.i.i19

test14__1.i.i19:                                  ; preds = %test13__1.i.i18
  %spec.select14.i.i = and i1 %157, %154
  %164 = and i1 %spec.select14.i.i, %142
  br i1 %164, label %then0__1.i5, label %test15__1.i.i20

test15__1.i.i20:                                  ; preds = %test14__1.i.i19
  %165 = and i1 %spec.select14.i.i, %146
  br i1 %165, label %then0__1.i5, label %test16__1.i.i21

test16__1.i.i21:                                  ; preds = %test15__1.i.i20
  %166 = icmp eq i64 %60, 128
  %spec.select16.i.i = and i1 %166, %140
  %167 = and i1 %spec.select16.i.i, %142
  br i1 %167, label %continue__3.sink.split.i14, label %test17__1.i.i22

test17__1.i.i22:                                  ; preds = %test16__1.i.i21
  %168 = and i1 %spec.select16.i.i, %146
  br i1 %168, label %then1__1.i9, label %test18__1.i.i24

test18__1.i.i24:                                  ; preds = %test17__1.i.i22
  %spec.select18.i.i23 = and i1 %166, %148
  %169 = and i1 %spec.select18.i.i23, %142
  br i1 %169, label %then0__1.i5, label %test19__1.i.i25

test19__1.i.i25:                                  ; preds = %test18__1.i.i24
  %170 = and i1 %spec.select18.i.i23, %146
  br i1 %170, label %then0__2.i8, label %test20__1.i.i26

test20__1.i.i26:                                  ; preds = %test19__1.i.i25
  %spec.select20.i.i = and i1 %166, %151
  %171 = and i1 %spec.select20.i.i, %142
  br i1 %171, label %then0__1.i5, label %test21__1.i.i27

test21__1.i.i27:                                  ; preds = %test20__1.i.i26
  %172 = and i1 %spec.select20.i.i, %146
  br i1 %172, label %then0__1.i5, label %test22__1.i.i28

test22__1.i.i28:                                  ; preds = %test21__1.i.i27
  %spec.select22.i.i = and i1 %166, %154
  %173 = and i1 %spec.select22.i.i, %142
  br i1 %173, label %then2__1.i10, label %Microsoft__Quantum__Samples__Inverse1C__body.exit

Microsoft__Quantum__Samples__Inverse1C__body.exit: ; preds = %test22__1.i.i28
  %174 = and i1 %spec.select22.i.i, %146
  %..i.i29 = select i1 %174, i64 186, i64 0
  %175 = and i64 %..i.i29, 8
  %.not.i4 = icmp eq i64 %175, 0
  %extract109 = lshr i64 %..i.i29, 4
  %extract.t110 = trunc i64 %extract109 to i2
  %extract113 = lshr i64 %..i.i29, 6
  %extract.t114 = trunc i64 %extract113 to i2
  br i1 %.not.i4, label %continue__1.i7, label %then0__1.i5

then0__1.i5:                                      ; preds = %Microsoft__Quantum__Samples__Inverse1C__body.exit, %test21__1.i.i27, %test20__1.i.i26, %test18__1.i.i24, %test15__1.i.i20, %test14__1.i.i19, %test12__1.i.i17, %test9__1.i.i13, %test7__1.i.i11, %test5__1.i.i8, %test3__1.i.i5, %test1__1.i.i2
  %merge.i.i31106.off4 = phi i2 [ %extract.t110, %Microsoft__Quantum__Samples__Inverse1C__body.exit ], [ 0, %test21__1.i.i27 ], [ -2, %test20__1.i.i26 ], [ 1, %test18__1.i.i24 ], [ -1, %test15__1.i.i20 ], [ 1, %test14__1.i.i19 ], [ 0, %test12__1.i.i17 ], [ -2, %test9__1.i.i13 ], [ -1, %test7__1.i.i11 ], [ -2, %test5__1.i.i8 ], [ 1, %test3__1.i.i5 ], [ 0, %test1__1.i.i2 ]
  %merge.i.i31106.off6 = phi i2 [ %extract.t114, %Microsoft__Quantum__Samples__Inverse1C__body.exit ], [ 1, %test21__1.i.i27 ], [ 1, %test20__1.i.i26 ], [ -2, %test18__1.i.i24 ], [ 1, %test15__1.i.i20 ], [ 1, %test14__1.i.i19 ], [ -2, %test12__1.i.i17 ], [ -2, %test9__1.i.i13 ], [ 0, %test7__1.i.i11 ], [ 0, %test5__1.i.i8 ], [ 0, %test3__1.i.i5 ], [ 0, %test1__1.i.i2 ]
  tail call void @__quantum__qis__x__body(%Qubit* null)
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %continue__1.i7

continue__1.i7:                                   ; preds = %then0__1.i5, %Microsoft__Quantum__Samples__Inverse1C__body.exit
  %merge.i.i31100.off4 = phi i2 [ %merge.i.i31106.off4, %then0__1.i5 ], [ %extract.t110, %Microsoft__Quantum__Samples__Inverse1C__body.exit ]
  %merge.i.i31100.off6 = phi i2 [ %merge.i.i31106.off6, %then0__1.i5 ], [ %extract.t114, %Microsoft__Quantum__Samples__Inverse1C__body.exit ]
  switch i2 %merge.i.i31100.off4, label %continue__2.i12 [
    i2 1, label %then0__2.i8
    i2 -2, label %then1__1.i9
    i2 -1, label %then2__1.i10
  ]

then0__2.i8:                                      ; preds = %continue__1.i7, %test19__1.i.i25, %test10__1.i.i14, %test6__1.i.i10
  %merge.i.i31100.off6133 = phi i2 [ %merge.i.i31100.off6, %continue__1.i7 ], [ 0, %test6__1.i.i10 ], [ 1, %test10__1.i.i14 ], [ -2, %test19__1.i.i25 ]
  tail call void @__quantum__qis__s__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__s__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__s__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__s__body(%Qubit* null)
  br label %continue__2.i12

then1__1.i9:                                      ; preds = %continue__1.i7, %test17__1.i.i22, %test13__1.i.i18, %test4__1.i.i7
  %merge.i.i31100.off6139 = phi i2 [ %merge.i.i31100.off6, %continue__1.i7 ], [ 0, %test4__1.i.i7 ], [ -2, %test13__1.i.i18 ], [ 1, %test17__1.i.i22 ]
  tail call void @__quantum__qis__z__body(%Qubit* null)
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %continue__2.i12

then2__1.i10:                                     ; preds = %continue__1.i7, %test22__1.i.i28, %test11__1.i.i15, %test2__1.i.i4
  %merge.i.i31100.off6145 = phi i2 [ %merge.i.i31100.off6, %continue__1.i7 ], [ 0, %test2__1.i.i4 ], [ 1, %test11__1.i.i15 ], [ -2, %test22__1.i.i28 ]
  tail call void @__quantum__qis__s__adj(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %continue__2.i12

continue__2.i12:                                  ; preds = %then2__1.i10, %then1__1.i9, %then0__2.i8, %continue__1.i7
  %merge.i.i31100.off6127 = phi i2 [ %merge.i.i31100.off6145, %then2__1.i10 ], [ %merge.i.i31100.off6139, %then1__1.i9 ], [ %merge.i.i31100.off6133, %then0__2.i8 ], [ %merge.i.i31100.off6, %continue__1.i7 ]
  switch i2 %merge.i.i31100.off6127, label %Microsoft__Quantum__Samples__ApplyLogicalClifford__body.9.exit [
    i2 1, label %continue__3.sink.split.i14
    i2 -2, label %then1__2.i13
  ]

then1__2.i13:                                     ; preds = %continue__2.i12, %test8__1.i.i12
  tail call void @__quantum__qis__s__adj(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %continue__3.sink.split.i14

continue__3.sink.split.i14:                       ; preds = %then1__2.i13, %continue__2.i12, %test16__1.i.i21
  tail call void @__quantum__qis__s__adj(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__s__adj(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %Microsoft__Quantum__Samples__ApplyLogicalClifford__body.9.exit

Microsoft__Quantum__Samples__ApplyLogicalClifford__body.9.exit: ; preds = %continue__3.sink.split.i14, %continue__2.i12, %exit__1
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Result* nonnull inttoptr (i64 4 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Result* nonnull inttoptr (i64 5 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Result* nonnull inttoptr (i64 6 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__cz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*), %Result* nonnull inttoptr (i64 7 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 5 to %Qubit*))
  %176 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 4 to %Result*))
  br i1 %176, label %test1__1.i18, label %condContinue__1.i15

condContinue__1.i15:                              ; preds = %Microsoft__Quantum__Samples__ApplyLogicalClifford__body.9.exit
  %177 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 5 to %Result*))
  br i1 %177, label %test1__1.i18, label %condContinue__2.i16

condContinue__2.i16:                              ; preds = %condContinue__1.i15
  %178 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 6 to %Result*))
  br i1 %178, label %test1__1.i18, label %condContinue__3.i17

condContinue__3.i17:                              ; preds = %condContinue__2.i16
  %179 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 7 to %Result*))
  br i1 %179, label %test1__1.i18, label %Microsoft__Quantum__Samples__Recover__body.15.exit

test1__1.i18:                                     ; preds = %condContinue__3.i17, %condContinue__2.i16, %condContinue__1.i15, %Microsoft__Quantum__Samples__ApplyLogicalClifford__body.9.exit
  %180 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 4 to %Result*))
  br i1 %180, label %test2__1.i23, label %condContinue__4.i19

condContinue__4.i19:                              ; preds = %test1__1.i18
  %181 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 5 to %Result*))
  br i1 %181, label %test2__1.i23, label %condContinue__5.i20

condContinue__5.i20:                              ; preds = %condContinue__4.i19
  %182 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 6 to %Result*))
  br i1 %182, label %test2__1.i23, label %condTrue__6.i21

condTrue__6.i21:                                  ; preds = %condContinue__5.i20
  %183 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 7 to %Result*))
  br i1 %183, label %then1__1.i22, label %test2__1.i23

then1__1.i22:                                     ; preds = %condTrue__6.i21
  tail call void @__quantum__qis__x__body(%Qubit* null)
  br label %Microsoft__Quantum__Samples__Recover__body.15.exit

test2__1.i23:                                     ; preds = %condTrue__6.i21, %condContinue__5.i20, %condContinue__4.i19, %test1__1.i18
  %184 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 4 to %Result*))
  br i1 %184, label %test3__1.i28, label %condContinue__7.i24

condContinue__7.i24:                              ; preds = %test2__1.i23
  %185 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 5 to %Result*))
  br i1 %185, label %test3__1.i28, label %condTrue__8.i25

condTrue__8.i25:                                  ; preds = %condContinue__7.i24
  %186 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 6 to %Result*))
  br i1 %186, label %condContinue__9.i26, label %test3__1.i28

condContinue__9.i26:                              ; preds = %condTrue__8.i25
  %187 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 7 to %Result*))
  br i1 %187, label %test3__1.i28, label %then2__1.i27

then2__1.i27:                                     ; preds = %condContinue__9.i26
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.15.exit

test3__1.i28:                                     ; preds = %condContinue__9.i26, %condTrue__8.i25, %condContinue__7.i24, %test2__1.i23
  %188 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 4 to %Result*))
  br i1 %188, label %test4__1.i33, label %condContinue__10.i29

condContinue__10.i29:                             ; preds = %test3__1.i28
  %189 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 5 to %Result*))
  br i1 %189, label %test4__1.i33, label %condTrue__11.i30

condTrue__11.i30:                                 ; preds = %condContinue__10.i29
  %190 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 6 to %Result*))
  br i1 %190, label %condContinue__12.i31, label %test4__1.i33

condContinue__12.i31:                             ; preds = %condTrue__11.i30
  %191 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 7 to %Result*))
  br i1 %191, label %then3__1.i32, label %test4__1.i33

then3__1.i32:                                     ; preds = %condContinue__12.i31
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.15.exit

test4__1.i33:                                     ; preds = %condContinue__12.i31, %condTrue__11.i30, %condContinue__10.i29, %test3__1.i28
  %192 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 4 to %Result*))
  br i1 %192, label %test5__1.i38, label %condContinue__13.i34

condContinue__13.i34:                             ; preds = %test4__1.i33
  %193 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 5 to %Result*))
  br i1 %193, label %condContinue__14.i35, label %test5__1.i38

condContinue__14.i35:                             ; preds = %condContinue__13.i34
  %194 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 6 to %Result*))
  br i1 %194, label %test5__1.i38, label %condContinue__15.i36

condContinue__15.i36:                             ; preds = %condContinue__14.i35
  %195 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 7 to %Result*))
  br i1 %195, label %test5__1.i38, label %then4__1.i37

then4__1.i37:                                     ; preds = %condContinue__15.i36
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.15.exit

test5__1.i38:                                     ; preds = %condContinue__15.i36, %condContinue__14.i35, %condContinue__13.i34, %test4__1.i33
  %196 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 4 to %Result*))
  br i1 %196, label %test6__1.i43, label %condContinue__16.i39

condContinue__16.i39:                             ; preds = %test5__1.i38
  %197 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 5 to %Result*))
  br i1 %197, label %condContinue__17.i40, label %test6__1.i43

condContinue__17.i40:                             ; preds = %condContinue__16.i39
  %198 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 6 to %Result*))
  br i1 %198, label %test6__1.i43, label %condContinue__18.i41

condContinue__18.i41:                             ; preds = %condContinue__17.i40
  %199 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 7 to %Result*))
  br i1 %199, label %then5__1.i42, label %test6__1.i43

then5__1.i42:                                     ; preds = %condContinue__18.i41
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.15.exit

test6__1.i43:                                     ; preds = %condContinue__18.i41, %condContinue__17.i40, %condContinue__16.i39, %test5__1.i38
  %200 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 4 to %Result*))
  br i1 %200, label %test7__1.i48, label %condContinue__19.i44

condContinue__19.i44:                             ; preds = %test6__1.i43
  %201 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 5 to %Result*))
  br i1 %201, label %condContinue__20.i45, label %test7__1.i48

condContinue__20.i45:                             ; preds = %condContinue__19.i44
  %202 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 6 to %Result*))
  br i1 %202, label %condContinue__21.i46, label %test7__1.i48

condContinue__21.i46:                             ; preds = %condContinue__20.i45
  %203 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 7 to %Result*))
  br i1 %203, label %test7__1.i48, label %then6__1.i47

then6__1.i47:                                     ; preds = %condContinue__21.i46
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.15.exit

test7__1.i48:                                     ; preds = %condContinue__21.i46, %condContinue__20.i45, %condContinue__19.i44, %test6__1.i43
  %204 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 4 to %Result*))
  br i1 %204, label %test8__1.i53, label %condContinue__22.i49

condContinue__22.i49:                             ; preds = %test7__1.i48
  %205 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 5 to %Result*))
  br i1 %205, label %condContinue__23.i50, label %test8__1.i53

condContinue__23.i50:                             ; preds = %condContinue__22.i49
  %206 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 6 to %Result*))
  br i1 %206, label %condContinue__24.i51, label %test8__1.i53

condContinue__24.i51:                             ; preds = %condContinue__23.i50
  %207 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 7 to %Result*))
  br i1 %207, label %then7__1.i52, label %test8__1.i53

then7__1.i52:                                     ; preds = %condContinue__24.i51
  tail call void @__quantum__qis__y__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.15.exit

test8__1.i53:                                     ; preds = %condContinue__24.i51, %condContinue__23.i50, %condContinue__22.i49, %test7__1.i48
  %208 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 4 to %Result*))
  br i1 %208, label %condContinue__25.i54, label %test9__1.i58

condContinue__25.i54:                             ; preds = %test8__1.i53
  %209 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 5 to %Result*))
  br i1 %209, label %test9__1.i58, label %condContinue__26.i55

condContinue__26.i55:                             ; preds = %condContinue__25.i54
  %210 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 6 to %Result*))
  br i1 %210, label %test9__1.i58, label %condContinue__27.i56

condContinue__27.i56:                             ; preds = %condContinue__26.i55
  %211 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 7 to %Result*))
  br i1 %211, label %test9__1.i58, label %then8__1.i57

then8__1.i57:                                     ; preds = %condContinue__27.i56
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.15.exit

test9__1.i58:                                     ; preds = %condContinue__27.i56, %condContinue__26.i55, %condContinue__25.i54, %test8__1.i53
  %212 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 4 to %Result*))
  br i1 %212, label %condContinue__28.i59, label %test10__1.i63

condContinue__28.i59:                             ; preds = %test9__1.i58
  %213 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 5 to %Result*))
  br i1 %213, label %test10__1.i63, label %condContinue__29.i60

condContinue__29.i60:                             ; preds = %condContinue__28.i59
  %214 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 6 to %Result*))
  br i1 %214, label %test10__1.i63, label %condContinue__30.i61

condContinue__30.i61:                             ; preds = %condContinue__29.i60
  %215 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 7 to %Result*))
  br i1 %215, label %then9__1.i62, label %test10__1.i63

then9__1.i62:                                     ; preds = %condContinue__30.i61
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.15.exit

test10__1.i63:                                    ; preds = %condContinue__30.i61, %condContinue__29.i60, %condContinue__28.i59, %test9__1.i58
  %216 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 4 to %Result*))
  br i1 %216, label %condContinue__31.i64, label %test11__1.i68

condContinue__31.i64:                             ; preds = %test10__1.i63
  %217 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 5 to %Result*))
  br i1 %217, label %test11__1.i68, label %condContinue__32.i65

condContinue__32.i65:                             ; preds = %condContinue__31.i64
  %218 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 6 to %Result*))
  br i1 %218, label %condContinue__33.i66, label %test11__1.i68

condContinue__33.i66:                             ; preds = %condContinue__32.i65
  %219 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 7 to %Result*))
  br i1 %219, label %test11__1.i68, label %then10__1.i67

then10__1.i67:                                    ; preds = %condContinue__33.i66
  tail call void @__quantum__qis__z__body(%Qubit* null)
  br label %Microsoft__Quantum__Samples__Recover__body.15.exit

test11__1.i68:                                    ; preds = %condContinue__33.i66, %condContinue__32.i65, %condContinue__31.i64, %test10__1.i63
  %220 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 4 to %Result*))
  br i1 %220, label %condContinue__34.i69, label %test12__1.i73

condContinue__34.i69:                             ; preds = %test11__1.i68
  %221 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 5 to %Result*))
  br i1 %221, label %test12__1.i73, label %condContinue__35.i70

condContinue__35.i70:                             ; preds = %condContinue__34.i69
  %222 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 6 to %Result*))
  br i1 %222, label %condContinue__36.i71, label %test12__1.i73

condContinue__36.i71:                             ; preds = %condContinue__35.i70
  %223 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 7 to %Result*))
  br i1 %223, label %then11__1.i72, label %test12__1.i73

then11__1.i72:                                    ; preds = %condContinue__36.i71
  tail call void @__quantum__qis__y__body(%Qubit* null)
  br label %Microsoft__Quantum__Samples__Recover__body.15.exit

test12__1.i73:                                    ; preds = %condContinue__36.i71, %condContinue__35.i70, %condContinue__34.i69, %test11__1.i68
  %224 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 4 to %Result*))
  br i1 %224, label %condContinue__37.i74, label %test13__1.i78

condContinue__37.i74:                             ; preds = %test12__1.i73
  %225 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 5 to %Result*))
  br i1 %225, label %condContinue__38.i75, label %test13__1.i78

condContinue__38.i75:                             ; preds = %condContinue__37.i74
  %226 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 6 to %Result*))
  br i1 %226, label %test13__1.i78, label %condContinue__39.i76

condContinue__39.i76:                             ; preds = %condContinue__38.i75
  %227 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 7 to %Result*))
  br i1 %227, label %test13__1.i78, label %then12__1.i77

then12__1.i77:                                    ; preds = %condContinue__39.i76
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.15.exit

test13__1.i78:                                    ; preds = %condContinue__39.i76, %condContinue__38.i75, %condContinue__37.i74, %test12__1.i73
  %228 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 4 to %Result*))
  br i1 %228, label %condContinue__40.i79, label %test14__1.i83

condContinue__40.i79:                             ; preds = %test13__1.i78
  %229 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 5 to %Result*))
  br i1 %229, label %condContinue__41.i80, label %test14__1.i83

condContinue__41.i80:                             ; preds = %condContinue__40.i79
  %230 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 6 to %Result*))
  br i1 %230, label %test14__1.i83, label %condContinue__42.i81

condContinue__42.i81:                             ; preds = %condContinue__41.i80
  %231 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 7 to %Result*))
  br i1 %231, label %then13__1.i82, label %test14__1.i83

then13__1.i82:                                    ; preds = %condContinue__42.i81
  tail call void @__quantum__qis__y__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.15.exit

test14__1.i83:                                    ; preds = %condContinue__42.i81, %condContinue__41.i80, %condContinue__40.i79, %test13__1.i78
  %232 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 4 to %Result*))
  br i1 %232, label %condContinue__43.i84, label %test15__1.i88

condContinue__43.i84:                             ; preds = %test14__1.i83
  %233 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 5 to %Result*))
  br i1 %233, label %condContinue__44.i85, label %test15__1.i88

condContinue__44.i85:                             ; preds = %condContinue__43.i84
  %234 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 6 to %Result*))
  br i1 %234, label %condContinue__45.i86, label %test15__1.i88

condContinue__45.i86:                             ; preds = %condContinue__44.i85
  %235 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 7 to %Result*))
  br i1 %235, label %test15__1.i88, label %then14__1.i87

then14__1.i87:                                    ; preds = %condContinue__45.i86
  tail call void @__quantum__qis__y__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.15.exit

test15__1.i88:                                    ; preds = %condContinue__45.i86, %condContinue__44.i85, %condContinue__43.i84, %test14__1.i83
  %236 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 4 to %Result*))
  br i1 %236, label %condContinue__46.i89, label %Microsoft__Quantum__Samples__Recover__body.15.exit

condContinue__46.i89:                             ; preds = %test15__1.i88
  %237 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 5 to %Result*))
  br i1 %237, label %condContinue__47.i90, label %Microsoft__Quantum__Samples__Recover__body.15.exit

condContinue__47.i90:                             ; preds = %condContinue__46.i89
  %238 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 6 to %Result*))
  br i1 %238, label %condContinue__48.i91, label %Microsoft__Quantum__Samples__Recover__body.15.exit

condContinue__48.i91:                             ; preds = %condContinue__47.i90
  %239 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 7 to %Result*))
  br i1 %239, label %then15__1.i92, label %Microsoft__Quantum__Samples__Recover__body.15.exit

then15__1.i92:                                    ; preds = %condContinue__48.i91
  tail call void @__quantum__qis__y__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  br label %Microsoft__Quantum__Samples__Recover__body.15.exit

Microsoft__Quantum__Samples__Recover__body.15.exit: ; preds = %then15__1.i92, %condContinue__48.i91, %condContinue__47.i90, %condContinue__46.i89, %test15__1.i88, %then14__1.i87, %then13__1.i82, %then12__1.i77, %then11__1.i72, %then10__1.i67, %then9__1.i62, %then8__1.i57, %then7__1.i52, %then6__1.i47, %then5__1.i42, %then4__1.i37, %then3__1.i32, %then2__1.i27, %then1__1.i22, %condContinue__3.i17
  tail call void @__quantum__qis__y__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 4 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 3 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 4 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 3 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* null)
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 8 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  ret void
}

declare void @__quantum__qis__mz__body(%Qubit*, %Result*) local_unnamed_addr

declare i1 @__quantum__qir__read_result(%Result*) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="6" }
