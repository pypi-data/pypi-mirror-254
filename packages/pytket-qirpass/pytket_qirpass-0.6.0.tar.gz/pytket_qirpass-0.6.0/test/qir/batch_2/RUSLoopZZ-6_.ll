; ModuleID = 'RUSLoopZZ-6.bc'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [6 x i8] c"0_t0r\00"
@1 = internal constant [6 x i8] c"1_t1r\00"
@2 = internal constant [6 x i8] c"2_t2r\00"
@3 = internal constant [6 x i8] c"aux_1\00"
@4 = internal constant [6 x i8] c"aux_2\00"

define void @Microsoft__Quantum__Samples__RepeatUntilSuccess__RepeatUntilSuccess() #0 {
entry:
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__t__body(%Qubit* null)
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__t__adj(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  call void @__quantum__qis__reset__body(%Qubit* null)
  %0 = call i1 @__quantum__qis__read_result__body(%Result* null)
  br i1 %0, label %then0__3, label %continue__7

then0__3:                                         ; preds = %entry
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue__7

continue__7:                                      ; preds = %then0__3, %entry
  call void @__quantum__qis__h__body(%Qubit* null)
  %1 = call i1 @__quantum__qis__read_result__body(%Result* null)
  br i1 %1, label %else__1, label %then0__4

then0__4:                                         ; preds = %continue__7
  call void @__quantum__qis__t__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__t__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Result* nonnull inttoptr (i64 1 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  %2 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %2, label %then0__6, label %continue__13

then0__6:                                         ; preds = %then0__4
  call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %continue__13

continue__13:                                     ; preds = %then0__6, %then0__4
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  %3 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 1 to %Result*))
  %4 = xor i1 %3, true
  br i1 %3, label %then0__7, label %continue__9

then0__7:                                         ; preds = %continue__13
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  br label %continue__9

else__1:                                          ; preds = %continue__7
  call void @__quantum__qis__z__body(%Qubit* null)
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %continue__9

continue__9:                                      ; preds = %else__1, %then0__7, %continue__13
  %result2.0 = phi i1 [ false, %else__1 ], [ %4, %then0__7 ], [ %4, %continue__13 ]
  %5 = xor i1 %result2.0, true
  %6 = select i1 %1, i1 true, i1 %5
  br i1 %6, label %then0__8, label %continue__16

then0__8:                                         ; preds = %continue__9
  call void @__quantum__qis__t__body(%Qubit* null)
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__t__adj(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 2 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* null)
  %7 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %7, label %then0__10, label %continue__20

then0__10:                                        ; preds = %then0__8
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue__20

continue__20:                                     ; preds = %then0__10, %then0__8
  call void @__quantum__qis__h__body(%Qubit* null)
  %8 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %8, label %else__2, label %then0__11

then0__11:                                        ; preds = %continue__20
  call void @__quantum__qis__t__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__t__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Result* nonnull inttoptr (i64 3 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  %9 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %9, label %then0__13, label %continue__26

then0__13:                                        ; preds = %then0__11
  call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %continue__26

continue__26:                                     ; preds = %then0__13, %then0__11
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  %10 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 3 to %Result*))
  %11 = xor i1 %10, true
  br i1 %10, label %then0__14, label %continue__16

then0__14:                                        ; preds = %continue__26
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  br label %continue__16

else__2:                                          ; preds = %continue__20
  call void @__quantum__qis__z__body(%Qubit* null)
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %continue__16

continue__16:                                     ; preds = %else__2, %then0__14, %continue__26, %continue__9
  %result1.0.in = phi i1 [ %1, %continue__9 ], [ %8, %continue__26 ], [ %8, %then0__14 ], [ %8, %else__2 ]
  %result2.2 = phi i1 [ %result2.0, %continue__9 ], [ %11, %continue__26 ], [ %11, %then0__14 ], [ %result2.0, %else__2 ]
  %result1.0 = xor i1 %result1.0.in, true
  %12 = select i1 %result1.0, i1 %result2.2, i1 false
  br i1 %12, label %continue__29, label %then0__15

then0__15:                                        ; preds = %continue__16
  call void @__quantum__qis__t__body(%Qubit* null)
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__t__adj(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 4 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* null)
  %13 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 4 to %Result*))
  br i1 %13, label %then0__17, label %continue__33

then0__17:                                        ; preds = %then0__15
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue__33

continue__33:                                     ; preds = %then0__17, %then0__15
  call void @__quantum__qis__h__body(%Qubit* null)
  %14 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 4 to %Result*))
  %15 = xor i1 %14, true
  br i1 %14, label %else__3, label %then0__18

then0__18:                                        ; preds = %continue__33
  call void @__quantum__qis__t__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__t__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Result* nonnull inttoptr (i64 5 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  %16 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 5 to %Result*))
  br i1 %16, label %then0__20, label %continue__39

then0__20:                                        ; preds = %then0__18
  call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %continue__39

continue__39:                                     ; preds = %then0__20, %then0__18
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  %17 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 5 to %Result*))
  %18 = xor i1 %17, true
  br i1 %17, label %then0__21, label %continue__29

then0__21:                                        ; preds = %continue__39
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  br label %continue__29

else__3:                                          ; preds = %continue__33
  call void @__quantum__qis__z__body(%Qubit* null)
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %continue__29

continue__29:                                     ; preds = %else__3, %then0__21, %continue__39, %continue__16
  %result1.1 = phi i1 [ %result1.0, %continue__16 ], [ %15, %continue__39 ], [ %15, %then0__21 ], [ %15, %else__3 ]
  %result2.4 = phi i1 [ %result2.2, %continue__16 ], [ %18, %continue__39 ], [ %18, %then0__21 ], [ %result2.2, %else__3 ]
  %19 = select i1 %result1.1, i1 %result2.4, i1 false
  br i1 %19, label %continue__42, label %then0__22

then0__22:                                        ; preds = %continue__29
  call void @__quantum__qis__t__body(%Qubit* null)
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__t__adj(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 6 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* null)
  %20 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 6 to %Result*))
  br i1 %20, label %then0__24, label %continue__46

then0__24:                                        ; preds = %then0__22
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue__46

continue__46:                                     ; preds = %then0__24, %then0__22
  call void @__quantum__qis__h__body(%Qubit* null)
  %21 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 6 to %Result*))
  %22 = xor i1 %21, true
  br i1 %21, label %else__4, label %then0__25

then0__25:                                        ; preds = %continue__46
  call void @__quantum__qis__t__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__t__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Result* nonnull inttoptr (i64 7 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  %23 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 7 to %Result*))
  br i1 %23, label %then0__27, label %continue__52

then0__27:                                        ; preds = %then0__25
  call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %continue__52

continue__52:                                     ; preds = %then0__27, %then0__25
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  %24 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 7 to %Result*))
  %25 = xor i1 %24, true
  br i1 %24, label %then0__28, label %continue__42

then0__28:                                        ; preds = %continue__52
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  br label %continue__42

else__4:                                          ; preds = %continue__46
  call void @__quantum__qis__z__body(%Qubit* null)
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %continue__42

continue__42:                                     ; preds = %else__4, %then0__28, %continue__52, %continue__29
  %result1.2 = phi i1 [ %result1.1, %continue__29 ], [ %22, %continue__52 ], [ %22, %then0__28 ], [ %22, %else__4 ]
  %result2.6 = phi i1 [ %result2.4, %continue__29 ], [ %25, %continue__52 ], [ %25, %then0__28 ], [ %result2.4, %else__4 ]
  %26 = select i1 %result1.2, i1 %result2.6, i1 false
  br i1 %26, label %continue__55, label %then0__29

then0__29:                                        ; preds = %continue__42
  call void @__quantum__qis__t__body(%Qubit* null)
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__t__adj(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 8 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* null)
  %27 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 8 to %Result*))
  br i1 %27, label %then0__31, label %continue__59

then0__31:                                        ; preds = %then0__29
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue__59

continue__59:                                     ; preds = %then0__31, %then0__29
  call void @__quantum__qis__h__body(%Qubit* null)
  %28 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 8 to %Result*))
  %29 = xor i1 %28, true
  br i1 %28, label %else__5, label %then0__32

then0__32:                                        ; preds = %continue__59
  call void @__quantum__qis__t__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__t__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Result* nonnull inttoptr (i64 9 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  %30 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 9 to %Result*))
  br i1 %30, label %then0__34, label %continue__65

then0__34:                                        ; preds = %then0__32
  call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %continue__65

continue__65:                                     ; preds = %then0__34, %then0__32
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  %31 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 9 to %Result*))
  %32 = xor i1 %31, true
  br i1 %31, label %then0__35, label %continue__55

then0__35:                                        ; preds = %continue__65
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  br label %continue__55

else__5:                                          ; preds = %continue__59
  call void @__quantum__qis__z__body(%Qubit* null)
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %continue__55

continue__55:                                     ; preds = %else__5, %then0__35, %continue__65, %continue__42
  %result1.3 = phi i1 [ %result1.2, %continue__42 ], [ %29, %continue__65 ], [ %29, %then0__35 ], [ %29, %else__5 ]
  %result2.8 = phi i1 [ %result2.6, %continue__42 ], [ %32, %continue__65 ], [ %32, %then0__35 ], [ %result2.6, %else__5 ]
  %33 = select i1 %result1.3, i1 %result2.8, i1 false
  br i1 %33, label %continue__68, label %then0__36

then0__36:                                        ; preds = %continue__55
  call void @__quantum__qis__t__body(%Qubit* null)
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Qubit* null)
  call void @__quantum__qis__t__adj(%Qubit* null)
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 10 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* null)
  %34 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 10 to %Result*))
  br i1 %34, label %then0__38, label %continue__72

then0__38:                                        ; preds = %then0__36
  call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue__72

continue__72:                                     ; preds = %then0__38, %then0__36
  call void @__quantum__qis__h__body(%Qubit* null)
  %35 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 10 to %Result*))
  br i1 %35, label %else__6, label %then0__39

then0__39:                                        ; preds = %continue__72
  call void @__quantum__qis__t__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__cnot__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__t__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Result* nonnull inttoptr (i64 11 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  %36 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 11 to %Result*))
  br i1 %36, label %then0__41, label %continue__78

then0__41:                                        ; preds = %then0__39
  call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %continue__78

continue__78:                                     ; preds = %then0__41, %then0__39
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  %37 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 11 to %Result*))
  br i1 %37, label %then0__42, label %continue__68

then0__42:                                        ; preds = %continue__78
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__z__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  br label %continue__68

else__6:                                          ; preds = %continue__72
  call void @__quantum__qis__z__body(%Qubit* null)
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  br label %continue__68

continue__68:                                     ; preds = %else__6, %then0__42, %continue__78, %continue__55
  call void @__quantum__qis__rz__body(double 0x4001B6E192EBBE42, %Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__h__body(%Qubit* null)
  call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 12 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* null)
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Result* nonnull inttoptr (i64 13 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*), %Result* nonnull inttoptr (i64 14 to %Result*))
  call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  %38 = call i1 @__quantum__qis__read_result__body(%Result* nonnull inttoptr (i64 14 to %Result*))
  br i1 %38, label %then0__45, label %continue__84

then0__45:                                        ; preds = %continue__68
  call void @__quantum__qis__x__body(%Qubit* nonnull inttoptr (i64 2 to %Qubit*))
  br label %continue__84

continue__84:                                     ; preds = %then0__45, %continue__68
  call void @__quantum__rt__tuple_start_record_output()
  ;call void @__quantum__rt__result_record_output(%Result* nonnull inttoptr (i64 12 to %Result*), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @0, i64 0, i64 0))
  ;call void @__quantum__rt__result_record_output(%Result* nonnull inttoptr (i64 13 to %Result*), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @1, i64 0, i64 0))
  call void @__quantum__rt__result_record_output(%Result* null, i8* getelementptr inbounds ([6 x i8], [6 x i8]* @3, i64 0, i64 0))
  call void @__quantum__rt__result_record_output(%Result* nonnull inttoptr (i64 1 to %Result*), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @4, i64 0, i64 0))
  call void @__quantum__rt__result_record_output(%Result* nonnull inttoptr (i64 14 to %Result*), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @2, i64 0, i64 0))
  call void @__quantum__rt__tuple_end_record_output()
  ret void
}

declare %Qubit* @__quantum__rt__qubit_allocate()

declare void @__quantum__qis__h__body(%Qubit*)

declare void @__quantum__qis__t__body(%Qubit*)

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*)

declare void @__quantum__qis__t__adj(%Qubit*)

declare %Result* @__quantum__rt__result_get_zero()

declare void @__quantum__rt__result_update_reference_count(%Result*, i32)

declare %Result* @__quantum__qis__m__body(%Qubit*)

declare void @__quantum__qis__reset__body(%Qubit*)

declare %Result* @__quantum__rt__result_get_one()

declare i1 @__quantum__rt__result_equal(%Result*, %Result*)

declare void @__quantum__qis__x__body(%Qubit*)

declare void @__quantum__qis__z__body(%Qubit*)

declare void @__quantum__qis__rz__body(double, %Qubit*)

declare void @__quantum__rt__qubit_release(%Qubit*)

declare void @__quantum__rt__tuple_start_record_output()

declare void @__quantum__rt__result_record_output(%Result*, i8*)

declare void @__quantum__rt__tuple_end_record_output()

declare void @__quantum__qis__mz__body(%Qubit*, %Result*)

declare i1 @__quantum__qis__read_result__body(%Result*)

attributes #0 = { "EntryPoint" "maxQubitIndex"="2" "maxResultIndex"="14" "requiredQubits"="3" "requiredResults"="15" }
